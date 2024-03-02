# DJA5># main_app/urls.py
from django.urls import path
#from views import the def display_data
from .views import display_data 
# from .views import set_session, get_session

urlpatterns = [
    path('', display_data, name='data_page'),
    path('addtwo/', display_data, name='addtwo_page'),
    path('reset/', display_data, name='reset_page'),
    # path('reset', display_data, name='reset_page'),
    # path('set_session/', set_session, name='set_session'),
    # path('get_session/', get_session, name='get_session'),
]
