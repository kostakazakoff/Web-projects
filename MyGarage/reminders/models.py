from django.db import models, router
from django.contrib.auth import get_user_model
from vehicles.models import Vehicles
from django.db.models.deletion import Collector

#TODO: validators
UserModel = get_user_model()


class Reminder(models.Model):
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
    )
    on_odometer = models.PositiveIntegerField(
        null=True,
        blank=True,
    )
    photo = models.ImageField(
        upload_to='images/',
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
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='vehicle',
    )

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        try:
            current = Reminder.objects.get(pk=self.pk)
            if current.photo != self.photo:
                current.photo.delete()
        except:
            pass

        return super().save(*args, **kwargs)
    
    def delete(self, using=None, keep_parents=False):
        try:
            current = Reminder.objects.get(pk=self.pk)
            current.photo.delete()
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
