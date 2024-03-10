# DJA10>main_app>forms.py
from django import forms
# Built in form for creating users
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Post

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    first_name = forms.CharField(max_length=30, help_text='Required. Must be longer than 1 character.')
    last_name = forms.CharField(max_length=30, help_text='Required. Must be longer than 1 character.')

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'autofocus': True}))
    password = forms.CharField(widget=forms.PasswordInput)

    # custom validation on the entire form after the individual field-level validations are done.
    def clean(self):
        # super().clean() calls clean method of parent (forms.Form) ensuring default cleaning executes
        cleaned_data = super().clean()
        # A dictionary containing the validated and cleaned values of the form fields.
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            pass

        return cleaned_data
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']