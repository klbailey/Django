# DJA10>main_app>admin.py
from django.contrib import admin
from .models import CustomUser, Post

# Register the CustomUser model with the Django admin
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_active', 'is_staff')
    ordering = ('email',)

# Register the Post model with the Django admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'created_at')
    search_fields = ('user__email', 'content')
    list_filter = ('created_at',)
    ordering = ('-created_at',)  # Show the latest posts first