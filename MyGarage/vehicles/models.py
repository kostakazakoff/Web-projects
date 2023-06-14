# Vehicles
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import (
    MinLengthValidator,
    MaxLengthValidator,
    URLValidator,
    )
from my_garage.core.validators import (
    value_is_17_chars,
    year_is_valid,
    )
from django.utils import timezone


class VehicleChoices(models.TextChoices):
    BRAND = 'brand'
    VIN = 'vin'
    PLATE = 'plate'
    YEAR = 'year'


class Vehicles(models.Model):
    class Meta:
        ordering = ('-year',)

    brand = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    model = models.CharField(
        max_length=30,
        null=True,
        blank=True
    )
    vin = models.CharField(
        max_length=17,
        validators=[value_is_17_chars],
        null=True,
        blank=True,
        unique=True,
    )
    plate = models.CharField(
        max_length=10,
        null=False,
        blank=False,
        unique=True,
    )
    odometer = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    year = models.CharField(
        max_length=4,
        validators=[year_is_valid],
        null=False,
        blank=False
    )
    date_of_purchase = models.DateField(
        blank=True,
        null=True,
        default=timezone.now(),
    )
    price = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=0
    )
    photo = models.ImageField(
        upload_to='images',
        blank=True,
        null=True,
    )
    
    # TODO: slug validator if slug field is added to admin panel
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    
    def save(self, *args, **kwargs):

        # Delete old image file from media if exist
        try:
            obj = Vehicles.objects.get(id=self.id)
            if obj.photo != self.photo:
                obj.photo.delete()
        except:
            pass

        super().save(*args, **kwargs)

        # Auto generate slug
        if not self.slug:
            self.slug = slugify(f'{self.brand}-{self.plate}')

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('vehicle details', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.brand} {self.model}'
