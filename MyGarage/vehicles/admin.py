from django.contrib import admin
from vehicles.models import Vehicles

@admin.register(Vehicles)
class VehiclesAdmin(admin.ModelAdmin):
    pass
