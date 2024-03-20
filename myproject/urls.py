'''
URL configuration for the project. Defines routes for admin interface and recipe-related actions.
Routes are mapped to view functions in the recipes application, enabling API endpoints for creating,
retrieving a specific recipe, and listing all recipe IDs.
'''

from django.contrib import admin
from django.urls import include, path
from recipes.views import create_recipe, get_recipe, get_all_recipe_ids

urlpatterns = [
    path('admin/', admin.site.urls),  # Route for the built-in Django admin interface.
    
    # API endpoints for the recipes application:
    path('create_recipe/', create_recipe, name='create_recipe'),  # Endpoint to create a new recipe.
    path('get_recipe/<int:recipe_id>/', get_recipe, name='get_recipe'),  # Endpoint to retrieve a specific recipe by ID.
    path('get_all_recipe_ids/', get_all_recipe_ids, name='get_all_recipe_ids'),  # Endpoint to list all recipe IDs.
]
