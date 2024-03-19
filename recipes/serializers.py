# serializers.py
from rest_framework import serializers
from recipes.models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'user_id', 'description', 'ingredients', 'steps', 'diet', 'people', 'food_saved']

        