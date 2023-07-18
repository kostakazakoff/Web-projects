from django.contrib import admin
from django.urls import path
from .views import (
    create_reminder_view,
    edit_reminder_view,
    delete_reminder_view,
    list_reminders_view,
)

urlpatterns = [
    path('create-reminder/', create_reminder_view, name='create reminder'),
    path('', list_reminders_view, name='reminders'),
    path('<int:pk>/edit/', edit_reminder_view, name='edit reminder'),
    path('<int:pk>/delete/', delete_reminder_view, name='delete reminder'),
]