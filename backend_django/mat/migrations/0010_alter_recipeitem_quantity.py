# Generated by Django 4.2.3 on 2023-08-28 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mat', '0009_alter_fooditem_cost_per_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeitem',
            name='quantity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
