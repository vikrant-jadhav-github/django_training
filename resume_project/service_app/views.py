from django.shortcuts import render

# Create your views here.

def service(request):
    return render(request, 'service_app/service.html')