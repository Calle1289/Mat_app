# Generated by Django 4.2.3 on 2023-08-28 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mat', '0008_recipe_total_weight_alter_fooditem_cost_per_unit_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fooditem',
            name='cost_per_unit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='fooditem',
            name='weight_per_unit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='total_cost',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='total_weight',
            field=models.FloatField(blank=True, null=True),
        ),
    ]