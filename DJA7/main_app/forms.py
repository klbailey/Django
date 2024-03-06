# main_app>forms.py
from django import forms
from .models import UserProfile

# defines a new class that inherits from 'forms.ModelForm
class UserProfileForm(forms.ModelForm):
    # Meta gives from instructions saying form is connected to UserProfile model and should
    # include the fields so Django knows structure/behavior in relation to model
    class Meta:
        model = UserProfile
        fields = ['name', 'height', 'weight', 'diet']