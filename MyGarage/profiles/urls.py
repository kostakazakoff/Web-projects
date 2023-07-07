from .views import (
    CreateUserView,
    LoginProfileView,
    CreateProfileView,
    DeleteProfileView,
    EditProfileView,
    )
from django.urls import path
from django.contrib.auth.views import logout_then_login


urlpatterns = [
    path('create/', CreateUserView.as_view(), name='sign up'),
    path('login/', LoginProfileView.as_view(), name='sign in'),
    path('create/', CreateProfileView.as_view(), name='create profile'),
    path('<int:pk>/edit/', EditProfileView.as_view(), name='edit profile'),
    path('logout/', logout_then_login, name='sign out'),
    path('delete/', DeleteProfileView.as_view(), name='delete profile')
]