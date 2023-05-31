from django.urls import path

from vehicles.views import garage, service

urlpatterns = [
    path('', garage, name='garage'),
    path('service/', service, name='service'),
    path('service/<int:vehicle_id>/', service, name='service'),
]
