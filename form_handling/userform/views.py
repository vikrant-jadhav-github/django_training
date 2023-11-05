from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def showuserform(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['email'])
    else:
        form = UserForm()
    return render(request, 'userform/showuserform.html', {'form':form})