from django import forms
from .models import Reminder
from django.core.exceptions import ValidationError


class CreateReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        exclude = ['to_user', 'done']