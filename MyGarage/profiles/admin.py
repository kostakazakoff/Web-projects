from django.contrib import admin
from .models import AppUser, Profile

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    order_by = ['first_name', 'last_name']