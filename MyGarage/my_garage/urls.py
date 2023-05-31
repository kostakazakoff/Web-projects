from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehicles.urls')),
    path('reminders/', include('reminders.urls')),
    path('accounts/', include('accounts.urls')),
    path('service/', include('service.urls')),
]
