from django.contrib import admin
from django.urls import path, include
from service.views import add_service, edit_service, delete_service, vehicle_service_history

urlpatterns = [
    path('<int:pk>/', vehicle_service_history, name='vehicle service'),
    path('add/', add_service, name='add service'),
    path('<int:service_id>/edit/', edit_service, name='edit service'),
    path('<int:service_id>/delete/', delete_service, name='delete service'),
]
