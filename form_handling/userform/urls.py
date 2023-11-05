from django.urls import path
from . import views

urlpatterns = [
    path('userform/', views.showuserform),
    path('regisuccess/', views.regisuccess),
]