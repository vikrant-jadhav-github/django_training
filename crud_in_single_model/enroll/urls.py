from enroll import views
from django.urls import path

urlpatterns = [
    path('edit/<int:p_id>/', views.edit, name='edit'),
    path('delete/<int:p_id>/', views.delete, name='delete'),
]