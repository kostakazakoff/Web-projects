from django.urls import path
from vehicles.views import garage, edit_vehicle, delete_vehicle, add_vehicle

# TODO: ?
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', garage, name='garage'),
    path('add/', add_vehicle, name='add vehicle'),
    path('<int:id>/edit-vehicle', edit_vehicle, name='edit vehicle'),
    path('<int:id>/delete-vehicle', delete_vehicle, name='delete vehicle'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # ?
