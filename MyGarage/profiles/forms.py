from django import forms
from django.contrib.auth import forms as auth_forms
from django.shortcuts import render
# from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from .models import Profile


UserModel = get_user_model()

# TODO: Validations

class RegisterUserForm(auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email', 'password1', 'password2')


class LoginProfileForm(auth_forms.AuthenticationForm):
    pass


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name']
        widgets = {'user': forms.TextInput(attrs={'class': 'hidden'},)}


class EditPasswordForm(auth_forms.PasswordChangeForm):
    pass