from rest_framework import serializers
from recipes.models import Recipe

 # Serializer for the Recipe model for converting complex data types to JSON for API interaction.
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ['name', 'user_id', 'description', 'ingredients', 'steps', 'diet', 'people', 'food_saved']

        
