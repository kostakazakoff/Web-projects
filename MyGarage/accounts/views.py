from django.shortcuts import render, redirect

def login_page(request):
    return render(request, 'accounts/login-page.html')

def create_account(request):
    return render(request, 'accounts/create-account.html')

def edit_account(request, id):
    return render(request, 'accounts/edit-account.html')

def delete_account(request, id):
    return render(request, 'accounts/delete-account.html')
