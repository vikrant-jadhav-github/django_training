from django.shortcuts import render
from .forms import PersonForm
from .models import Person
from django.http import HttpResponseRedirect
from django.contrib import messages
# Create your views here.

def home(request):
    data = Person.objects.all()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            form = PersonForm()
            messages.success(request, 'Data inserted successfully')
    else:
        form = PersonForm()
    return render(request, 'enroll/home.html', {'form':form, 'data' : data})

def edit(request, p_id):
    if request.method == 'POST':
        pi = Person.objects.get(pk=p_id)
        form = PersonForm(request.POST, instance=pi)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        pi = Person.objects.get(pk=p_id)
        form = PersonForm(instance=pi)
    return render(request, 'enroll/editperson.html', {'form':form, 'id':p_id})

def delete(request, p_id):
    if request.method == 'POST':
        pi = Person.objects.get(pk=p_id)
        pi.delete()
        return HttpResponseRedirect('/')
    return render(request, 'enroll/home.html')