from django.forms import ModelForm
from django import forms
from .models import Vehicles


class CreateVehicleForm(ModelForm):

    class Meta:
        model = Vehicles
        exclude = ['slug']
