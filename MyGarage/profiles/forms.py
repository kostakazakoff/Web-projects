from typing import Any
from django import forms
from .models import Profile, UserModel
from django.contrib.auth import get_user_model


class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = UserModel
        exclude = ['created_on', 'user']
        widgets = {
            'password': forms.PasswordInput,
            'email': forms.EmailInput,
        }


class LoginProfileForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'label': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'label': 'Password'}))
