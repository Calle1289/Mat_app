from django.db import models
from django.contrib.postgres.fields import JSONField

class FoodList(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    food_list = models.ForeignKey(FoodList, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.FloatField()
    weight = models.FloatField()
    nutrition_data = JSONField()

    def __str__(self):
        return self.name

