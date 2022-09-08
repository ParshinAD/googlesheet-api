from django.urls import path
from gsapi import views

urlpatterns = [
    path('', views.test1, name='first_page'),
    path('test2/', views.test2, name='main'),
]
