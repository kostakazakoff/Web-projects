from django.shortcuts import render, redirect
from django.views import generic as views
from .forms import CreateProfileForm, LoginProfileForm
from django.contrib.auth import get_user_model, authenticate, login, logout


UserModel = get_user_model()

#TODO:
def create_profile(request):
    form = CreateProfileForm(request.POST or None)

    if form.is_valid():
        UserModel.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password'],
        )
        form.save()
        return redirect('sign in')
    
    context = {'form': form, 'title': 'Sign up'}
    return render(request, 'profiles/create-profile.html', context=context)


def login_profile(request):
    print(f'User: {request.user}')
    form = LoginProfileForm(request.POST or None)

    if form.is_valid():
        user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        if user:
            login(request, user)
            return redirect('garage')
    
    context = {'form': form, 'title': 'Sign in'}
    return render(request, 'profiles/login-profile.html', context)


class EditProfileView(views.UpdateView):
    template_name = 'profiles/edit-profile.html'
    # model = EditProfile


class DeleteProfileView(views.DeleteView):
    template_name = 'profiles/delete-profile.html'


def logout_profile(request):
    logout(request)
    return redirect('sign in')
