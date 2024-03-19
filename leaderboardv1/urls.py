from django.urls import path
from .views import Leaderboardv1ListView, Leaderboardv1CreateView

urlpatterns = [
    path('', Leaderboardv1ListView.as_view(), name='leaderboardv1_list'),
    path('add/', Leaderboardv1CreateView.as_view(), name='add_leaderboardv1_entry'),
]
