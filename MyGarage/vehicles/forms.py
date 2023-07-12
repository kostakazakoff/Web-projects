from django.utils import timezone
from typing import Any
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from .models import Vehicles
from django.contrib.auth import get_user_model
from my_garage.core.validators import validate_max_date


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

    #TODO:
    # def clean_date_of_purchase(self):
    #     max_value = timezone.localdate(timezone.now())
    #     value = self.cleaned_data('date_of_purchase')
    #     if value > max_value:
    #         raise ValidationError("Invalid date of purchase. It can't be after current date")
    #     return value
    