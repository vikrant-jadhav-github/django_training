from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.crick_home),
    path('players/', views.crick_players),
]