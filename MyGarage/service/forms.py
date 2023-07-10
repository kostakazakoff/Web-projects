from django import forms
from .models import Service
from django.core.exceptions import ValidationError


class AddServiceForm(forms.ModelForm):

    class Meta:
        model = Service
        fields = '__all__'
        widgets = {
            'date': forms.TextInput(attrs={'type': 'date'}),
            'date_deadline': forms.TextInput(attrs={'type': 'date'}),
            'vehicle': forms.TextInput(attrs={'hidden': True, 'readonly': True}),
        }
        labels = {'vehicle': ''}
        

    def clean(self):
        cleaned_data = super().clean()
        vehicle = cleaned_data.get('vehicle')
        service_odometer = cleaned_data.get('odometer')
        vehicle_odometer = vehicle.odometer

        if service_odometer > vehicle_odometer:
            msg = f'Odometer must be max {vehicle_odometer}. Update your vehicle odometer'
            self.add_error('odometer', msg)
        

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
