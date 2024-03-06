#main_app>urls.py
from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.index, name='home'),
    # defines with ormat 'user/some_number/' where some_number is an integer representing the user's ID.
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),
]