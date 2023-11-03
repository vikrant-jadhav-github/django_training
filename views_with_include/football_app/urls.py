from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.football_home),
    path('players/', views.football_players),
]