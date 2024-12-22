from .views import (
    create_user_view,
    LoginProfileView,
    DeleteProfileView,
    edit_profile_view,
    password_change_view,
    )
from django.urls import path
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    path('create/', create_user_view, name='sign up'),
    path('login/', LoginProfileView.as_view(), name='sign in'),
    path('logout/', logout_then_login, name='sign out'),
    path('edit/', edit_profile_view, name='edit profile'),
    path('password/', password_change_view, name='password change'),
    path('<int:pk>/delete/', DeleteProfileView.as_view(), name='delete profile')
]