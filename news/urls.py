from django.urls import path
from . import views

urlpatterns = [
    path('newss/', views.newss, name='newss')
]
