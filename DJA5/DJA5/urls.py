"""
URL configuration for DJA5 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# DJA5>DJA5>urls.py
from django.contrib import admin
from django.urls import include, path
from main_app.views import display_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', display_data, name='data_page'),  # Empty path for the root URL
    path('addtwo/', display_data, name='addtwo_page'),
    path('reset/', display_data, name='reset_page'),  
    path('main_app/', include('main_app.urls')),
]
