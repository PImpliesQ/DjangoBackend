from django.db import models
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    meals_made = models.IntegerField(default=0)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# Create your models here.


class Recipe(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)
    user_id = models.CharField(max_length=255)
    description = models.TextField()
    ingredients = models.TextField()
    steps = models.TextField()
    diet = models.CharField(max_length=255)
    people = models.IntegerField()
    food_saved = models.IntegerField()

    class Meta:
        db_table = 'Recipe'