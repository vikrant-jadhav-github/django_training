from django.contrib import admin
from person_app.models import Person

# Register your models here.

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'email', 'p_id')
