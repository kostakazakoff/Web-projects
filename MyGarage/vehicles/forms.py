from django import forms
from django.forms import ModelForm
from .models import Vehicles


class CreateVehicleForm(ModelForm):

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
        }
