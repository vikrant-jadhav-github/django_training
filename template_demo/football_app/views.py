from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'football/football_home.html')

def players(request):
    return render(request, 'football/fplayers.html')