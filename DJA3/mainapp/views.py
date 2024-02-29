# Create your views here.
# DJA3/DJA3/mainapp/views.py
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import os

def index(request):
    return render(request, 'mainapp/index.html')

def display_name(request):
    return render(request, 'mainapp/display_name.html', {'name': 'Kathy'})  # Replace 'Your Name' with your actual name


def display_food(request):
    image_path = os.path.join(settings.STATIC_URL, 'sushi.jpg')
    context = {
        'food_name': 'Sushi',  
        'food_image_url': image_path,  
    }
    return render(request, 'mainapp/display_food.html', context)

def display_vacation(request):
    context = {
        'destination_name': 'A warm ocean wave',
        'destination_image_url': '/static/wave.jpg', 
    }
    return render(request, 'mainapp/display_vacation.html', context)