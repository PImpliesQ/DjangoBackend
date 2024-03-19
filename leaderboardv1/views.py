from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Leaderboardv1Entry
from .models import Student

class Leaderboardv1ListView(ListView):
    model = Student
    template_name = 'leaderboardv1/leaderboardv1_list.html'
    context_object_name = 'students'
    queryset = Student.objects.all().order_by('-points')  # This line is correct

class Leaderboardv1CreateView(CreateView):
    model = Leaderboardv1Entry
    fields = ['player_name', 'score']
    success_url = reverse_lazy('leaderboardv1_list')
# Create your views here.
