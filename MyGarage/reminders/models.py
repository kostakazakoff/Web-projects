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

    def clear_media(self):
        if self.photo:
            self.photo.delete()

    def clean(self):
        if self.on_odometer and self.to_vehicle and self.to_vehicle.odometer > self.on_odometer:
            raise ValidationError(f'Odometer must be at least {self.to_vehicle.odometer}')
        if not self.on_odometer and not self.on_date:
            raise ValidationError('You have to specify a reminder date or odometer')

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        print(self.photo)
        try:
            current = Reminder.objects.get(pk=self.pk)
            if not self.photo or current.photo.url != self.photo.url:
                # destroy(str(current.photo))
                current.photo.delete()
        except:
            pass

        return super().save(*args, **kwargs)
    
    def delete(self, using=None, keep_parents=False):
        try:
            # destroy(str(self.photo))
            self.photo.delete()
        except:
            pass

        if self.pk is None:
            raise ValueError(
                f"{self._meta.object_name} object can't be deleted because its \
                    {self._meta.pk.attname} attribute is set to None."
            )
        
        using = using or router.db_for_write(self.__class__, instance=self)
        collector = Collector(using=using, origin=self)
        collector.collect([self], keep_parents=keep_parents)
        return collector.delete()
