# DJA4>main_app>forms.py
from django import forms

# Fields with built-in validation rules 
class MyForm(forms.Form):
    # character field w/max 100 chars strint
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    # Email Field ensures input is valid email address (must have @ and a . somewhere after
    email = forms.EmailField()
    favorite_food = forms.CharField(max_length=100)
