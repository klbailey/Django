# main_app/forms.py
from django import forms
from .models import Post
#  Specifies a model form with a single field named 'post' which is a text area
class PostForm(forms.ModelForm):
    # class 'Meta' inside a form is a container class used to define metadata & configurations for form
    # allows me to provide additional info oabout form and how it should behave
    class Meta:
        model = Post
        fields = ['post']