from django.contrib import admin

from vehicles.models import Vehicles, Service

@admin.register(Vehicles)
class VehiclesAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'price', 'vehicle')