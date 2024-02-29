# Inside first_project/first_app/urls.py
#access to funciton path:
from django.urls import path
# imports views.py in current folder
from . import views


urlpatterns = [
    # r tells Python to interpret as raw string so it won't escape any special characters
    # similar to @app.route in flask (regex? path(r'^$', views.index)?)
    # removed r after 1st assignment
    path('', views.index),
    path('current_datetime/', views.current_datetime, name='current_datetime'),
]