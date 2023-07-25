from mat.models import FoodList, FoodItem
from exeee import livsmedelsverket_lista
import os
import django

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_django.settings")

# Initialize Django
django.setup()

food_data = livsmedelsverket_lista

# Create FoodList instance
food_list = FoodList.objects.create(name="My Food List")

# Loop through food data and create FoodItem instances associated with the FoodList
for food_name, food_info in food_data.items():
    food_item = FoodItem.objects.create(
        food_list=food_list,
        name=food_name,
        price=food_info["pris"],
        weight=food_info["vikt"],
        nutrition_data=food_info["Naringsvarde"],
    )
