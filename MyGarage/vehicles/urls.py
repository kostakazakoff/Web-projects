from django.urls import path
from vehicles.views import (
    # edit_vehicle,
    # update_odometer,
    # add_vehicle,
    # delete_vehicle,
    GarageView,
    AddVehicleView,
    EditVehicleView,
    UpdateOdometerView,
    VehicleDeleteView,
    )
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', GarageView.as_view(), name='garage'),
    path('add/', AddVehicleView.as_view(), name='add vehicle'),
    path('<int:pk>/edit-vehicle', EditVehicleView.as_view(), name='edit vehicle'),
    path('<int:pk>/delete-vehicle', VehicleDeleteView.as_view(), name='delete vehicle'),
    path('<int:pk>/update-odometer', UpdateOdometerView.as_view(), name='update odometer'),
]
