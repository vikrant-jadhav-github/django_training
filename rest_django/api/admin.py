from django.contrib import admin
from .models import Person, User
# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'age']


