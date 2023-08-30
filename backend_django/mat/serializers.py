from rest_framework import serializers
from django.contrib.auth.models import User
from .models import FoodItem, Recipe, RecipeItem

class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = '__all__'  # This will include all fields from the model, including the automatically created 'id' field.

class RecipeItemSerializer(serializers.ModelSerializer):
    food_item = serializers.PrimaryKeyRelatedField(queryset=FoodItem.objects.all())
    class Meta:
        model = RecipeItem
        fields = ['food_item', 'quantity']

class RecipeSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    items = RecipeItemSerializer(many=True)

    class Meta:
        model = Recipe
        fields = '__all__'

    def compute_totals(self, items_data):
        total_nutrition = {}
        total_cost = 0
        total_weight = 0  # Initialize the total weight accumulator

        for item_data in items_data:
            food_item = item_data['food_item']

            if not food_item.weight_per_unit or not food_item.cost_per_unit:
                return total_nutrition, None, None  # Return None for total_cost and total_weight if any item is missing its weight or cost

            # If weight_per_unit is available, use it. We've already checked for its presence above.
            quantity_ratio = item_data['quantity'] / food_item.weight_per_unit

            # Accumulate the total weight for the food item
            total_weight += food_item.weight_per_unit * item_data['quantity']

            # Calculate nutrition if nutritional_data exists
            if food_item.nutritional_data:
                for key, value in food_item.nutritional_data.items():
                    value_numeric = float(value['Varde'])
                    total_nutrition[key] = total_nutrition.get(key, 0) + value_numeric * quantity_ratio

            # Calculate cost. We've already checked for cost_per_unit's presence above.
            total_cost += food_item.cost_per_unit * quantity_ratio

        return total_nutrition, total_cost, total_weight


    def create(self, validated_data):
        items_data = validated_data.pop('items')
        total_nutrition, total_cost, total_weight = self.compute_totals(items_data)  # Unpack the third return value

        user = self.context['request'].user
        recipe = Recipe.objects.create(total_nutrition=total_nutrition, total_cost=total_cost, total_weight=total_weight, **validated_data)
        
        for item_data in items_data:
            RecipeItem.objects.create(recipe=recipe, **item_data)

        return recipe

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items')
        total_nutrition, total_cost, total_weight = self.compute_totals(items_data)  # Unpack the third return value
        instance.total_nutrition = total_nutrition
        instance.total_cost = total_cost
        instance.total_weight = total_weight  # Update the total weight of the instance

        # Update the Recipe instance
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        # Update or create RecipeItem instances
        for item_data in items_data:
            RecipeItem.objects.update_or_create(recipe=instance, food_item=item_data['food_item'], defaults={'quantity': item_data['quantity']})
        
        return instance


class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})
    password2 = serializers.CharField(write_only=True, required=True, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email', 'first_name', 'last_name']
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({"password": "The two passwords differ."})
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        return user