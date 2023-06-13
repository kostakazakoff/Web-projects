from django.forms import ModelForm
from .models import Vehicles


class CreateVehicleForm(ModelForm):

    class Meta:
        model = Vehicles
        exclude = ['slug']

    # TODO: ImageField style
