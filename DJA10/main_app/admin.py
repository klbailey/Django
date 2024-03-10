# DJA10>main_app>admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Register your models here.
# Defines custom admin class inherits from built in UserAdmin class; extend functionality
# provided by 'UserAdmin' & customizing it for CustomUser model
class CustomUserAdmin(UserAdmin):
    # Tell Django custom admin class intended for CustomUser model
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'is_active', 'is_staff']
    # for search queries
    search_fields = ['email', 'first_name', 'last_name']
    # default sorting order for the change list view
    ordering = ['email']
    # Tuple of 2 elemenet tuples where ea tuple is a section/group of fields in admin form
    fieldsets = (
        # string, dictionary of fields key to be included
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    # Used when adding new instanace of model 'Add' view of admin interface; allows to customize form
    # Here includes needed fields for creating a new user w/additional styling classes
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )
    # many to many relationships in horizontal layout; Django will display them in user-friendly way
    filter_horizontal = ()
    # Remove 'is_superuser' and 'groups' from list_filter
    list_filter = ('is_active', 'is_staff')
admin.site.register(CustomUser, CustomUserAdmin)
