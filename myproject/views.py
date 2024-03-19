from django.shortcuts import render

# Create your views here.
# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from recipes.models import Recipe
from recipes.serializers import RecipeSerializer

@api_view(['POST'])
def create_recipe(request):
    serializer = RecipeSerializer(data=request.data)
    if serializer.is_valid():
        recipe = serializer.save()
        return Response({'id': recipe.id}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET'])
def get_recipe(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)
    except Recipe.DoesNotExist:
        return Response(status=404)

@api_view(['GET'])
def get_all_recipe_ids(request):
    recipe_ids = Recipe.objects.values_list('id', flat=True)
    return Response({'ids': list(recipe_ids)})
