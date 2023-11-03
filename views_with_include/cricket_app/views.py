from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def crick_home(request):
    return HttpResponse("crick Home")

def crick_players(request):
    return HttpResponse("crick Players")