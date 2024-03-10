# DJA10>main_app>views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate #import alias?
from django.contrib.auth.forms import AuthenticationForm  # Import AuthenticationForm
from .forms import RegistrationForm, CustomLoginForm
# Create your views here.

def register(request):
    print("Register view executed")
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            auth_login(request, user)  # Change login to auth_login
            # Redirect to the news_feed view
            return redirect('news_feed')
        else:
            print("Form errors:", form.errors)
    else:
        form = RegistrationForm()
        

    return render(request, 'main_app/register.html', {'form': form})

    # if request.method == 'POST':
    #     form = RegistrationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         return redirect('news_feed')  
    # else:
    #     form = RegistrationForm()

    # return render(request, 'registration/register.html', {'form': form})

def news_feed(request):
    # Add logic to fetch and display news feed content
    return render(request, 'main_app/news_feed.html')


def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                auth_login(request, user)
                print("User authenticated successfully")
                return redirect('news_feed')
            else:
                print("User is None after authentication")
        else:
            print("Form is not valid")
    else:
        form = CustomLoginForm()

    return render(request, 'main_app/login.html', {'form': form})

    # if request.method == 'POST':
    #     form = AuthenticationForm(request, request.POST)
    #     if form.is_valid():
    #         user = form.get_user()
    #         auth_login(request, user)
    #         return redirect('news_feed')
    # else:
    #     form = AuthenticationForm()

    # return render(request, 'main_app/login.html', {'form': form})