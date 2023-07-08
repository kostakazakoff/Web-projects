from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import (
    RegisterUserForm,
    LoginProfileForm,
    EditProfileForm,
)
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile


UserModel = get_user_model()


class CreateUserView(LoginRequiredMixin, views.CreateView):

    template_name = 'profiles/create-profile.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('garage')
    extra_context = {'title': 'Sign up'}
    
    def form_valid(self, form):
        parent = super().form_valid(form)
        login(self.request, self.object)
        Profile.objects.create(user=self.object)
        return parent
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
            # return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class LoginProfileView(auth_views.LoginView):

    template_name = 'profiles/login-profile.html'
    form_class = LoginProfileForm
    extra_context = {'title': 'Sign in'}


class EditProfileView(LoginRequiredMixin, views.UpdateView):

    template_name = 'profiles/edit-profile.html'
    form_class = EditProfileForm
    model = Profile
    extra_context = {'title': 'Edit Profile'}
    success_url = reverse_lazy('garage')


class DeleteProfileView(LoginRequiredMixin, views.DeleteView):

    model = UserModel
    template_name = 'profiles/delete-profile.html'
    extra_context = {'title': 'Are you shure you want to delete this profile?'}
    success_url = reverse_lazy('sign in')
