from datetime import datetime
from django.shortcuts import render, HttpResponse, redirect


# Create your views here. Ubdex function is called when root is visited

def index(request):
    return HttpResponse('Name: Kathy Bailey Hines <br>Fave Movie: Dune <br> Fave Music: rap')

def current_datetime(request):
    current_time = datetime.now()
    return render(request, 'first_app/home.html', {'current_time': current_time})
