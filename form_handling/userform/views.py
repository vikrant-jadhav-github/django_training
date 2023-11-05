from django.shortcuts import render
from .forms import UserForm
from django.http import HttpResponseRedirect
# Create your views here.

def regisuccess(request):
    return render(request, 'userform/regisuccess.html')

def showuserform(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
            return HttpResponseRedirect('/uf/regisuccess')
    else:
        form = UserForm()
    return render(request, 'userform/showuserform.html', {'form':form})