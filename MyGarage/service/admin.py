from django.contrib import admin
from service.models import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    pass
