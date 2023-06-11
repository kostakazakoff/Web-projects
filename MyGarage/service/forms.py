from django.core.exceptions import ValidationError
from django.forms import ModelForm, forms
from .models import Service
from vehicles.models import Vehicles


class AddServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'

    def clean_odometer_deadline(self):
        deadline = self.cleaned_data['odometer_deadline']
        current = self.cleaned_data['odometer']

        if deadline and current:
            if deadline <= current:
                raise ValidationError(f'Deadline must be a greater value than {current}')

        return deadline

    def clean_date_deadline(self):
        deadline = self.cleaned_data['date_deadline']
        date_of_service = self.cleaned_data['date']

        if date_of_service and deadline:
            if deadline <= date_of_service:
                raise ValidationError(f'Deadline date must be after {date_of_service}')

        return deadline
