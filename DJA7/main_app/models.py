# DJA7>main_app>models.py
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    # tuple (represents possible choice) used for ordered pairing; 1st is stored in database 2nd is displayed to user
    DIET_CHOICES = [
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('no_preference', 'No Preference'),
    ]
    # define properties(name, height, weight, diet)
    name = models.CharField(max_length=264, unique = True)
    height = models.FloatField()
    weight = models.FloatField()
    # name of field.char field to store text(length, choices from tuple)
    # the diet field is a CharField that stores text representing the dietary preference of the user. 
    # It can only store values that are specified in the DIET_CHOICES list.
    diet = models.CharField(max_length=15, choices=DIET_CHOICES)

    # method defines human-readable string of an object
    def __str__(self):
        # returns itself by user name
        return self.name
