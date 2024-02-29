from django.shortcuts import render, HttpResponse, redirect

# Create your views here. Ubdex function is called when root is visited

def index(request):
    return HttpResponse('Name: Kathy Bailey Hines <br>Fave Movie: Dune <br> Fave Music: rap')
