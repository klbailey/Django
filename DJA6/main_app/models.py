# main_app>models.py
from django.db import models
from django.conf import settings

# Create your models here.
class Post(models.Model):
    post = models.TextField()
    def __str__(self):
        return self.post