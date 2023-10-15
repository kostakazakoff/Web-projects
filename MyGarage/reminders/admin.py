from django.contrib import admin
from .models import Reminder

@admin.register(Reminder)
class ReminderAdmin(admin.ModelAdmin):
    list_display = ['title', 'on_date', 'on_odometer', 'to_vehicle', 'to_service', 'to_user', 'id']
