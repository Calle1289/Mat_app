from mat.models import FoodList, FoodItem
from mat.scripts.exeee import livsmedelsverket_lista

def run():
    # Import logic
    food_data = livsmedelsverket_lista
    food_list = FoodList.objects.create(name="My Food List")

    for food_name, food_info in food_data.items():
        FoodItem.objects.update_or_create(
            food_list=food_list,
            name=food_name,
            defaults={
                "price": food_info.get("pris", None),  # This will return None if "pris" doesn't exist
                "weight": food_info.get("vikt", None),  # This will return None if "vikt" doesn't exist
                "nutrition_data": food_info.get("Naringsvarden", None) # This will return None if "Naringsvarden" doesn't
            }
        )

