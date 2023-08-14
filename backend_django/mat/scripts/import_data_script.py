from mat.models import FoodList, FoodItem
from mat.scripts.exeee import livsmedelsverket_lista

def import_data():

    # Your import logic
    food_data = livsmedelsverket_lista
    food_list = FoodList.objects.create(name="My Food List")

    for food_name, food_info in food_data.items():
        food_item = FoodItem.objects.create(
            food_list=food_list,
            name=food_name,
            price=food_info["pris"],
            weight=food_info["vikt"],
            nutrition_data=food_info["Naringsvarde"],
        )