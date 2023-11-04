from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    p_id = models.IntegerField()

    def __str__(self):
        return self.name