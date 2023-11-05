from django import forms

class UserForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)