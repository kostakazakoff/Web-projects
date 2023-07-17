from django import forms
from .models import Reminder


class BaseReminderForm(forms.ModelForm):
    class Meta:
        model = Reminder
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(),
            'on_date': forms.TextInput(attrs={
                'type': 'date'
            }),
        }


class CreateServiceReminderForm(BaseReminderForm):
    class Meta(BaseReminderForm.Meta):
        exclude = ['to_user']
        widgets = {
            'to_service': forms.TextInput(attrs={
                'readonly': True,
            }),
            'on_date': forms.TextInput(attrs={
                'readonly': True,
            }),
            'on_odometer': forms.TextInput(attrs={
                'readonly': True,
            }),
        }


class CreateReminderForm(BaseReminderForm):
    class Meta(BaseReminderForm.Meta):
        exclude = ['to_user', 'on_odometer', 'to_service']