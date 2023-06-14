from typing import Any, Dict
from django import forms
from .models import Service
from django.core.exceptions import ValidationError


class AddServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'
        

    # def clean(self):
    #     cleaned_data = super().clean()
    #     date = cleaned_data.get('date')
    #     vehicle = cleaned_data.get('vehicle')
    #     purchase_date = vehicle.date_of_purchase

    #     if date < purchase_date:
    #         # raise ValidationError(f'Date of service must be greater than {purchase_date}')
    #         msg = f'Date of service must be greater than {purchase_date}'
    #         self.add_error('date', msg)
        

    def clean_odometer_deadline(self):
        deadline = self.cleaned_data['odometer_deadline']
        current = self.cleaned_data['odometer']

        if deadline and current:
            if deadline <= current:
                raise ValidationError(f'Deadline value must be greater than {current}')

        return deadline


    def clean_date_deadline(self):
        date_deadline = self.cleaned_data['date_deadline']
        date_of_service = self.cleaned_data['date']

        if date_of_service and date_deadline:
            if date_deadline <= date_of_service:
                raise ValidationError(f'Deadline date must be after {date_of_service}')

        return date_deadline
