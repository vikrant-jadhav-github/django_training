from django.urls import path
from . import views

urlpatterns = [
    path('personview/api', views.PersonAPI.as_view()),
    path('personview/api/<int:pk>', views.PersonAPI.as_view()),
]