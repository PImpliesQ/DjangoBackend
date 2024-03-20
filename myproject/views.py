"""
Defines view functions for handling recipe-related API requests, including creating a new recipe,
retrieving a specific recipe by ID, and listing all recipe IDs. Uses Django Rest Framework (DRF)
for request handling and serialization.
Tested using Postman 
"""


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

@api_view(['POST'])
def create_recipe(request):
    # Create a new recipe, returning the new recipe ID or validation errors.
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        recipe = serializer.save()
        return Response({'id': recipe.id}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_recipe(request, recipe_id):
    # Retrieve and return a specific recipe by ID or 404 if not found.
    try:
        serializer = RecipeSerializer(Recipe.objects.get(pk=recipe_id))
        return Response(serializer.data)
    except Recipe.DoesNotExist:
        return Response(status=404)

@api_view(['GET'])
def get_all_recipe_ids(request):
    # Return a list of all recipe IDs.
    return Response({'ids': list(Recipe.objects.values_list('id', flat=True))})
