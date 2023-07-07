from django.contrib import admin
from .models import AppUser, Profile

@admin.register(AppUser)
class AppUserAdmin(admin.ModelAdmin):
    fields = ['email', 'password']

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass