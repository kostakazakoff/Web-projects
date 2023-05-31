from django.urls import path
from vehicles.views import garage

urlpatterns = [
    path('', garage, name='garage'),
]
