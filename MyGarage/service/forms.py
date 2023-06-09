from django.forms import ModelForm, forms
from .models import Service


class AddServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = '__all__'