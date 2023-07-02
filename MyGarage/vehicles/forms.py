from typing import Any
from django import forms
from django.forms import ModelForm
from .models import Vehicles
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class CreateVehiclesForm(ModelForm):
    # TODO: Hide to_user field label

    class Meta:
        model = Vehicles
        exclude = ['slug']
        widgets = {
            'brand': forms.TextInput(attrs={'placeholder': 'Max 30 characters'}),
            'model': forms.TextInput(attrs={'placeholder': 'Max 30 characters'}),
            'vin': forms.TextInput(attrs={'placeholder': 'Enter the VIN code here'}),
            'plate': forms.TextInput(attrs={'placeholder': 'Max 10 characters'}),
            'odometer': forms.TextInput(attrs={'placeholder': 'Enter the odometer value here'}),
            'year': forms.TextInput(attrs={'placeholder': 'Year of manufacture in format YYYY'}),
            'date_of_purchase': forms.TextInput(attrs={'type': 'date'}),
            'to_user': forms.TextInput(attrs={'style': 'display:none'}),
        }
        labels = {'to_user': ''}

    # def save(self) -> Any:
    #     instance = super().save()
    #     instance.to_user = user_id
    #     instance.save()
    #     return instance
    #     return super().save()
