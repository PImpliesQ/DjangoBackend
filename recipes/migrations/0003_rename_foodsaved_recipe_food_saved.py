# Generated by Django 5.0.3 on 2024-03-19 15:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("recipes", "0002_recipe"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="foodsaved",
            new_name="food_saved",
        ),
    ]