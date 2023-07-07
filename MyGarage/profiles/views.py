from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import (
    RegisterUserForm,
    LoginProfileForm,
    CreateProfileForm,
)
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


class CreateUserView(views.CreateView):

    template_name = 'profiles/create-profile.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('garage')
    extra_context = {'title': 'Create profile'}

    def form_valid(self, form):
        parent = super().form_valid(form)
        login(self.request, self.object)
        return parent


class LoginProfileView(auth_views.LoginView):

    template_name = 'profiles/login-profile.html'
    form_class = LoginProfileForm
    extra_context = {'title': 'Sign in'}


class CreateProfileView(LoginRequiredMixin, views.CreateView):

    form_class = CreateProfileForm
    template_name = 'profiles/create-profile.html'
    success_url = reverse_lazy('garage')

    def get_initial(self):
        initial = super().get_initial()
        initial['user'] = self.request.user.pk
        return initial

#TODO:
class EditProfileView(LoginRequiredMixin, views.UpdateView):

    pass



class DeleteProfileView(views.FormView):

    extra_context = {'title': 'Are you shure you want to delete this profile?'}
