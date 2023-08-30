from django.db import models
from django.contrib.auth.models import User

class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    weight_per_unit = models.FloatField(null=True, blank=True)  # e.g., weight in grams
    nutritional_data = models.JSONField(null=True, blank=True)  # This can store data like {"protein": 5, "carbs": 20, ...}
    cost_per_unit = models.FloatField(null=True, blank=True)  # e.g., cost in your currency per unit/gram/...

    def __str__(self):
        return self.name

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    # Many-to-many relationship with FoodItem
    items = models.ManyToManyField(FoodItem, through='RecipeItem')
    # Computed fields
    total_nutrition = models.JSONField(null=True, blank=True)
    total_cost = models.FloatField(null=True, blank=True)
    total_weight = models.FloatField(null=True, blank=True)
    
class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.FloatField(null=True, blank=True)  # e.g., quantity in grams or units

