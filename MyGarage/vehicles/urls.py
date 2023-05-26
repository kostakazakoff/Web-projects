from django.urls import path

from vehicles.views import home, service

urlpatterns = [
    path('', home, name='home'),
    path('service/', service, name='service'),
    path('service/<int:vehicle_id>/', service, name='service'),
]
