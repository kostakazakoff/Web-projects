from .views import (
    CreateProfileView,
    LoginProfileView,
    EditProfileView,
    DeleteProfileView
    )
from django.urls import path
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    path('create/', CreateProfileView.as_view(), name='sign up'),
    path('login/', LoginProfileView.as_view(), name='sign in'),
    path('edit/', EditProfileView.as_view(), name='edit profile'),
    path('logout/', logout_then_login, name='sign out'),
    path('delete/', DeleteProfileView.as_view(), name='delete profile')
]