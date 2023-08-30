from mat.models import FoodItem
from mat.scripts.exeee import livsmedelsverket_lista

def run():
    # Import logic
    food_data = livsmedelsverket_lista

    for food_name, food_info in food_data.items():
        FoodItem.objects.update_or_create(
            name=food_name,
            defaults={
                "cost_per_unit": food_info.get("pris", None),  # This will return None if "pris" doesn't exist
                "weight_per_unit": food_info.get("vikt", None),  # This will return None if "vikt" doesn't exist
                "nutritional_data": food_info.get("Naringsvarden", None) # This will return None if "Naringsvarden" doesn't
            }
        )

