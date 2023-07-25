from django.urls import path
from vehicles.views import edit_vehicle, delete_vehicle, GarageView, add_vehicle, update_odometer
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', GarageView.as_view(), name='garage'),
    path('add/', add_vehicle, name='add vehicle'),
    path('<int:id>/edit-vehicle', edit_vehicle, name='edit vehicle'),
    path('<int:id>/delete-vehicle', delete_vehicle, name='delete vehicle'),
    path('<int:id>/update-odometer', update_odometer, name='update odometer'),
]
