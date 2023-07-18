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


class CreateReminderForm(BaseReminderForm):
    class Meta(BaseReminderForm.Meta):
        exclude = ['to_user', 'to_service']