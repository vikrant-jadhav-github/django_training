from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def football_home(request):
    return HttpResponse("football Home")

def football_players(request):
    return HttpResponse("football Players")