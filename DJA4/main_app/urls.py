# DJA4>main_app>urls.py
from django.urls import path
from .views import index, form_view

urlpatterns = [
    path('', index, name='index'),
    path('form_view/', form_view, name='form_view'),
]
