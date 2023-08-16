from django.db import models
from django.db.models import JSONField

class FoodList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    food_list = models.ForeignKey(FoodList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    nutrition_data = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name

