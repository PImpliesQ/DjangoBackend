from django.contrib.auth.models import AbstractUser
from django.db import models

class UserRole(models.TextChoices): # change to clerk user
    PLAYER = 'player', 'Player User'
    GAME_KEEPER = 'game_keeper', 'Game Keeper'
    DEVELOPER = 'developer', 'Developer'

class CustomUser(AbstractUser):
    role = models.CharField(
        max_length=50,
        choices=UserRole.choices,
        default=UserRole.PLAYER,
    )





