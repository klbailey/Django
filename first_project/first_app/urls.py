# Inside first_project/first_app/urls.py
#access to funciton path:
from django.urls import path
# imports views.py in current folder
from . import views


urlpatterns = [
    # r tells Python to interpret as raw string so it won't escape any special characters
    # similar to @app.route in flask (regex? path(r'^$', views.index)?)
    path(r'', views.index)
]