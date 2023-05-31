from django.contrib import admin
from django.urls import path
from accounts.views import (
    login_page,
    create_account,
    edit_account,
    delete_account,
)

urlpatterns = [
    path('login/', login_page, name='login page'),
    path('create-account/', create_account, name='create account'),
    path('<int:id>/edit-account/', edit_account, name='edit account'),
    path('<int:id>/delete-account/', delete_account, name='delete account'),
]