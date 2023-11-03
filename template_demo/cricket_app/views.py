from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'cricket/cricket_home.html')

def players(request):
    return render(request, 'cricket/cplayers.html')