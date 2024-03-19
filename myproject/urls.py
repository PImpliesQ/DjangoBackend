from django.contrib import admin
from django.urls import include, path
from django.urls import path
from recipes.views import create_recipe, get_recipe, get_all_recipe_ids

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create_recipe/', create_recipe, name='create_recipe'),
    path('get_recipe/<int:recipe_id>/', get_recipe, name='get_recipe'),
    path('get_all_recipe_ids/', get_all_recipe_ids, name='get_all_recipe_ids'),
]