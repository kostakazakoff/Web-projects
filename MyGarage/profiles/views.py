from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from .forms import (
    RegisterUserForm,
    LoginProfileForm,
    )
from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth import views as auth_views


class CreateProfileView(views.CreateView):
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


class EditProfileView(views.FormView):
    template_name = 'profiles/edit-profile.html'


class DeleteProfileView(views.FormView):
    extra_context = {'title': 'Are you shure you want to delete this profile?'}


# def create_profile(request):
#     form = CreateProfileForm(request.POST or None)

#     if form.is_valid():
#         print(form.cleaned_data)
#         user_exist = authenticate(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password']
#             )
#         if not user_exist:
#             new_user = UserModel.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 password=form.cleaned_data['password'],
#             )
#             form.cleaned_data['user'] = new_user
#             form.save()
#             return redirect('sign in')
    
#     context = {'form': form, 'title': 'Sign up'}
#     return render(request, 'profiles/create-profile.html', context=context)


# def login_profile(request):
#     print(f'User: {request.user}')
#     form = LoginProfileForm(request.POST or None)

#     if form.is_valid():
#         print(form.cleaned_data)
#         user = authenticate(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password']
#             )
#         if user:
#             logout(request)
#             login(request, user)
#             return redirect('garage')
    
#     context = {'form': form, 'title': 'Sign in'}
#     return render(request, 'profiles/login-profile.html', context)


# class EditProfileView(views.UpdateView):
#     template_name = 'profiles/edit-profile.html'
#     fields = ['first_name', 'last_name', 'username', 'email', 'password']
#     success_url = reverse_lazy('garage')


# class DeleteProfileView(views.DeleteView):
#     template_name = 'profiles/delete-profile.html'


# @login_required
# def logout_profile(request):
#     logout(request)
#     return redirect('sign in')


# def create_user(request):
#     form = CreateUserForm(request.POST or None)
#     if form.is_valid():
#         UserModel.objects.create_user(
#             username=form.cleaned_data['username'],
#             password=form.cleaned_data['password']
#             )
#         return redirect('sign in')
    
#     context = {'form': form, 'title': 'Sign up'}
    
#     return render(request, 'profiles/create-profile.html', context)
