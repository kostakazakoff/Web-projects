from django.urls import path

from vehicles.views import index, service

urlpatterns = [
    path('', index, name='home'),
    path('service/', service, name='service'),
    path('service/<int:vehicle_id>/', service, name='service'),
]