from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def view2(request):
    return HttpResponse("Hello from view 2")