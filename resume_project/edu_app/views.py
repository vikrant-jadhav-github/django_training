from django.shortcuts import render

# Create your views here.

def education(request):
    return render(request, 'edu_app/education.html')