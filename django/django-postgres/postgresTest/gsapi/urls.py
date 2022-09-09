from django.urls import path
from gsapi import views

urlpatterns = [
    path('test2/', views.test2, name='main'),
]
