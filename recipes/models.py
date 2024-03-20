from django.db import models

class Recipe(models.Model):
    # Defines attributes for a cooking recipe, including who created it and its dietary type.
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255) 
    diet = models.CharField(max_length=255)

    # Recipe specifics: description, ingredients, and the cooking steps.
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()

    # Serving size and impact on food savings.
    people = models.IntegerField()
    food_saved = models.IntegerField()

    class Meta:
        db_table = 'Recipe'  
