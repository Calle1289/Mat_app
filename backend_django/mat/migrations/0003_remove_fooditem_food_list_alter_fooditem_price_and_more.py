# Generated by Django 4.2.3 on 2023-08-18 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mat', '0002_alter_fooditem_price_alter_fooditem_weight'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fooditem',
            name='food_list',
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.DeleteModel(
            name='FoodList',
        ),
    ]
