# DJA3/DJA3/mainapp/urls.py
from django.urls import path
from .views import index, display_name, display_food, display_vacation

urlpatterns = [
    path('', index, name='index'),
    path('display_name/', display_name, name='display_name'),
    path('display_food/', display_food, name='display_food'),
    path('display_vacation/', display_vacation, name='display_vacation'),
]
