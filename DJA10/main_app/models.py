# DJA10>main_app>models.py
from django.conf import settings
from django.db import models
# Part of Django's authentication system
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Part of Django's validators system
from django.core.validators import MinLengthValidator, EmailValidator

# Create your models here.
# Define custom manager for user model(creates user instances)

class CustomUserManager(BaseUserManager):
    # Creates a regular user; Checks if email is provided and akes sure it's lowercase
    # then creates a new user instance w/provided info, sets password, saves to database,
    # returns the user instance
    def create_user(self, email, first_name, last_name, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # Similar to create_user but for superusers
    def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, first_name, last_name, password, **extra_fields)

# Extends AbstractBaseUser
    
class CustomUser(AbstractBaseUser):
    # ensure email is valid
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    # ensure that the length of both names is at least 2 characters; limit_value=2 is @ least 2
    first_name = models.CharField(max_length=30, validators=[MinLengthValidator(limit_value=2)])
    last_name = models.CharField(max_length=30, validators=[MinLengthValidator(limit_value=2)])
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Associates CustomUserManager w/CustomUser so we can use custom manager's methods for
    # creating users
    objects = CustomUserManager()

    # Email for authentication; name required
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # defines string representation of CustomUser instance and returns email when instance
    # is printed/used in string context
    def __str__(self):
        return self.email