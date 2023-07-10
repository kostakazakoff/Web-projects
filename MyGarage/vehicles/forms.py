from typing import Any
from django import forms
from django.forms import ModelForm
from .models import Vehicles
from django.contrib.auth import get_user_model


UserModel = get_user_model()


class CreateVehiclesForm(ModelForm):

    class Meta:
        model = Vehicles
        exclude = ['slug', 'to_user']
        widgets = {
            'brand': forms.TextInput(attrs={'placeholder': 'Max 30 characters'}),
            'model': forms.TextInput(attrs={'placeholder': 'Max 30 characters'}),
            'vin': forms.TextInput(attrs={'placeholder': 'Enter the VIN code here'}),
            'plate': forms.TextInput(attrs={'placeholder': 'Max 10 characters'}),
            'odometer': forms.TextInput(attrs={'placeholder': 'Enter the odometer value here'}),
            'year': forms.TextInput(attrs={'placeholder': 'Year of manufacture in format YYYY'}),
            'date_of_purchase': forms.TextInput(attrs={'type': 'date'}),
        }

