from typing import Any
from django import forms
from .models import Profile, UserModel


class CreateProfileForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm password'},)
        )
    class Meta:
        model = Profile
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'confirm_password',
            'user'
        ]
        widgets = {
            'password': forms.PasswordInput(),
            'email': forms.EmailInput(),
            'user': forms.TextInput(attrs={'style': 'display:none'})
        }
        labels = {'user': ''}
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if password != confirm_password:
            raise forms.ValidationError(
                'Password and password confirmation does not match.'
            )

class LoginProfileForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'label': 'Username'})
        )
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'label': 'Password'})
        )


class CreateUserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = [
            'username',
            'password',
            'email'
        ]
        widgets = {
            'username': forms.TextInput(
                attrs={'helptext': ''}, 
            ),
            'email': forms.EmailInput(
                attrs={'helptext': ''}, 
            ),
            'password': forms.PasswordInput(
                attrs={'helptext': ''}, 
            )
        }
