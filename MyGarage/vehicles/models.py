# Vehicles
from django.db import models, router
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth import get_user_model
from my_garage.core.validators import (
    value_is_17_chars,
    year_is_valid,
    validate_max_date,
)
from django.db.models.deletion import Collector


UserModel = get_user_model()


class Vehicles(models.Model):
    BRAND_MODEL_MAX_LEN = 30
    VIN_LEN = 17
    PLATE_LEN = 10
    YEAR_LEN = 4

    class Meta:
        ordering = ('-year',)

    brand = models.CharField(
        max_length=BRAND_MODEL_MAX_LEN,
        null=False,
        blank=False
    )
    model = models.CharField(
        max_length=BRAND_MODEL_MAX_LEN,
        null=True,
        blank=True
    )
    vin = models.CharField(
        max_length=VIN_LEN,
        validators=[value_is_17_chars],
        null=True,
        blank=True,
        unique=True,
    )
    plate = models.CharField(
        max_length=PLATE_LEN,
        null=False,
        blank=False,
        unique=True,
    )
    odometer = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    year = models.CharField(
        max_length=YEAR_LEN,
        validators=[year_is_valid],
        null=False,
        blank=False
    )
    date_of_purchase = models.DateField(
        blank=True,
        null=True,
        validators=[validate_max_date],
    )
    price = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=0,
    )
    photo = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    to_user = models.ForeignKey(
        UserModel,
        null=False,
        blank=True,
        on_delete=models.CASCADE,
        related_name='vehicles',
        editable=False,
    )

    def save(self, *args, **kwargs):
        # Delete old image file from media if exist
        try:
            current = Vehicles.objects.get(id=self.id)
            if current.photo != self.photo:
                current.photo.delete()
        except:
            pass

        super().save(*args, **kwargs)

        # Auto generate slug
        if not self.slug:
            self.slug = slugify(f'{self.brand}-{self.plate}')

        return super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):

        try:
            current = Vehicles.objects.get(id=self.id)
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

    # def get_absolute_url(self):
    #     return reverse('vehicle details', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.brand} {self.model}'
