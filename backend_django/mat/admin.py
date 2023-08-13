from django.contrib import admin
from .models import FoodList, FoodItem

admin.site.register(FoodList)
admin.site.register(FoodItem)