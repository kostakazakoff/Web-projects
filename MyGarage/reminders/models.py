from django.db import models, router
from django.contrib.auth import get_user_model
from service.models import Service
from vehicles.models import Vehicles
from django.db.models.deletion import Collector
from django.utils import timezone
from my_garage.core.validators import validate_min_date
from django.core.exceptions import ValidationError
# import cloudinary.api
# from cloudinary_storage.storage import MediaCloudinaryStorage
# from cloudinary.uploader import upload, destroy

UserModel = get_user_model()

class Reminder(models.Model):
    class Meta():
        ordering = ('on_date', 'on_odometer')

    TITLE_MAX_LEN = 30
    DESCRIPTION_MAX_LEN = 100

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=DESCRIPTION_MAX_LEN,
    )
    on_date = models.DateField(
        null=True,
        blank=True,
        validators=[validate_min_date]
    )
    on_odometer = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        upload_to='reminders/',
        # storage=MediaCloudinaryStorage(),
        blank=True,
        null=True,
    )
    to_user = models.ForeignKey(
        UserModel,
        null=False,
        blank=False,
        editable=False,
        on_delete=models.CASCADE,
    )
    to_vehicle = models.ForeignKey(
        Vehicles,
        null=True,
        blank=True,
        editable = False,
        on_delete=models.CASCADE,
    )
    to_service = models.ForeignKey(
        Service,
        null=True,
        blank=True,
        editable=False,
        on_delete=models.SET_NULL,
    )

    def clean(self):
        if self.on_odometer and self.to_vehicle and self.to_vehicle.odometer > self.on_odometer:
            raise ValidationError(f'Odometer must be at least {self.to_vehicle.odometer}')
        if not self.on_odometer and not self.on_date:
            raise ValidationError('You have to specify a reminder date or odometer')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        try:
            current = Reminder.objects.get(pk=self.pk)
            if not self.photo or current.photo.url != self.photo.url:
                # destroy(str(current.photo))
                current.photo.delete()
        except:
            pass

        super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
        if self.photo:
            self.photo.delete(save=False)

        super().delete(*args, **kwargs)
