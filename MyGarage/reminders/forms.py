from typing import Any, Dict
from django import forms
from .models import Reminder
from django.core.exceptions import ValidationError


class BaseReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        exclude = ['to_user', 'to_service', 'to_vehicle']
        widgets = {
            'description': forms.Textarea(),
            'on_date': forms.TextInput(attrs={
                'type': 'date'
            }),
        }


class CreateReminderForm(BaseReminderForm):
    class Meta(BaseReminderForm.Meta):
        exclude = ['on_odometer']


class EditServiceReminderForm(BaseReminderForm):
    pass


class EditReminderForm(CreateReminderForm):
    pass