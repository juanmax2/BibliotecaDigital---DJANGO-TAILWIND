from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'is_librarian', 'is_staff')
    
    fieldsets = UserAdmin.fieldsets + (
        ('Información Extra', {'fields': ('phone', 'birth_date', 'is_librarian')}),
    )