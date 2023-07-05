from django import forms
from django.contrib.auth import forms as auth_forms
from django.utils.translation import gettext_lazy as _
from .models import UserModel


class RegisterUserForm(auth_forms.UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = ''
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''


class LoginProfileForm(auth_forms.AuthenticationForm):
    pass


# class CreateProfileForm(forms.ModelForm):
#     confirm_password = forms.CharField(widget=forms.PasswordInput(
#         attrs={'placeholder': 'Confirm password'},)
#         )
#     class Meta:
#         model = Profile
#         fields = [
#             'username',
#             'first_name',
#             'last_name',
#             'email',
#             'password',
#             'confirm_password',
#             'user'
#         ]
#         widgets = {
#             'password': forms.PasswordInput(),
#             'email': forms.EmailInput(),
#             'user': forms.TextInput(attrs={'style': 'display:none'})
#         }
#         labels = {'user': ''}
    
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         confirm_password = cleaned_data.get('confirm_password')
#         if password != confirm_password:
#             raise forms.ValidationError(
#                 'Password and password confirmation does not match.'
#             )
