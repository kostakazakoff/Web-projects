from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('vehicles.urls')),
    path('reminders/', include('reminders.urls')),
    path('accounts/', include('accounts.urls')),
    path('service/', include('service.urls')),
    path('photos/', include('photos.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
