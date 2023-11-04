from django.shortcuts import render
from person_app.models import Person

# Create your views here.

def home(request):
    data = Person.objects.all()
    """ data = Person.objects.get(p_id=1) """
    return render(request, 'person_app/home.html', {'data':data})