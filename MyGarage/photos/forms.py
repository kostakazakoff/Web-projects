from django import forms
from .models import Photo


class CreatePhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'