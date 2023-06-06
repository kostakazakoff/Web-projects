from django.forms import ModelForm
from django import forms
from .models import Vehicles


class CreateVehicleForm(ModelForm):
    class Meta:
        model = Vehicles
        fields = '__all__'

    brand = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input_field'}
        )
    )
    model = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input_field'}
        )
    )
    vin = forms.CharField(
        label='VIN code',
        widget=forms.TextInput(
            attrs={'class': 'input_field'},
        )
    )
    plate = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input_field'}
        )
    )
    odometer = forms.CharField(
        widget=forms.NumberInput(
            attrs={'class': 'input_field'}
        )
    )
    year = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'input_field'}
        )
    )
    date_of_purchase = forms.DateField(
        widget=forms.DateInput(
            attrs={'class': 'input_field'}
        )
    )
    price = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={'class': 'input_field'}
        )
    )
    slug = forms.SlugField(
        widget=forms.TextInput(
            attrs={'class': 'input_field'}
        )
    )
    photo = forms.CharField(
        widget=forms.TextInput(
            attrs={'class': 'input_field'}
        )
    )
