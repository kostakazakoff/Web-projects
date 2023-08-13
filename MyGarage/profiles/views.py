from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import (
    RegisterUserForm,
    LoginProfileForm,
    EditProfileForm,
    EditPasswordForm,
)
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import views as auth_views
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


UserModel = get_user_model()


def create_user_view(request):
    form = RegisterUserForm(request.POST or None)

    if form.is_valid():
        form.save()
        obj = UserModel.objects.latest('pk')
        login(request, obj)
        return redirect('garage')

    context = {
        'form': form,
        'title': 'Sign Up'
    }

    return render(request, 'profiles/create-profile.html', context)


class LoginProfileView(auth_views.LoginView):

    template_name = 'profiles/login-profile.html'
    form_class = LoginProfileForm
    extra_context = {'title': 'Sign in'}


@login_required
def edit_profile_view(request):
    profile = Profile.objects.get(pk=request.user.pk)

    form = EditProfileForm(request.POST or None, instance=profile)

    if form.is_valid():
        form.save()
        direction = request.POST.get('direction')
        return redirect(direction)

    context = {
        'form': form,
        'title': request.user.email
    }
    return render(request, 'profiles/edit-profile.html', context)


@login_required
def password_change_view(request):
    form = EditPasswordForm(request.user, request.POST or None)
    
    if form.is_valid():
        user = form.save()
        update_session_auth_hash(request, user)
        return redirect('edit profile')
    
    context = {
        'form': form,
        'title': request.user.email
        }
    
    return render(request, 'profiles/change-password.html', context)


class DeleteProfileView(LoginRequiredMixin, views.DeleteView):
    model = UserModel
    template_name = 'profiles/delete-profile.html'
    extra_context = {'title': 'Are you shure you want to delete this profile?'}
    success_url = reverse_lazy('sign in')
