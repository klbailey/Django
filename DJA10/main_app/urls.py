# DJA10>main_app>urls.py
from django.urls import path
from .views import register, news_feed, user_login

urlpatterns = [
    path('', register, name='home'),  # Set the register view as the landing page
    path('register/', register, name='register'),
    path('news_feed/', news_feed, name='news_feed'),
    path('login/', user_login, name='user_login'),
]