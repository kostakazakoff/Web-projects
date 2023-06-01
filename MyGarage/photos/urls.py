from django.urls import path, include
from photos.views import (
    details_photo,
    add_photo,
    delete_photo,
)

urlpatterns = [
    path('add/', add_photo, name='add photo'),
    path('<int:pk>/details/', details_photo, name='details photo'),
    path('<int:pk>/delete/', delete_photo, name='delete photo'),
]