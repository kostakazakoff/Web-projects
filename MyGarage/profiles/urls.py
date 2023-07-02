from .views import (
    create_profile,
    login_profile,
    logout_profile,
    EditProfileView,
    DeleteProfileView
    )
from django.urls import path


urlpatterns = [
    path('create/', create_profile, name='sign up'),
    path('login/', login_profile, name='sign in'),
    path('logout/', logout_profile, name='sign out'),
    path('<int:pk>/edit/', EditProfileView.as_view(), name='edit profile'),
    path('<int:pk>/delete/', DeleteProfileView.as_view(), name='delete profile')
]