from django.urls import path
from vehicles.views import index, service

urlpatterns = [
    path('', index),
    # path('service', service),
    path('service/<int:vehicle_id>/', service),
]