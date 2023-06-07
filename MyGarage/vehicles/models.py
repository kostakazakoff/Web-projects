# Vehicles

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Vehicle_choices(models.TextChoices):
    BRAND = 'brand'
    VIN = 'vin'
    PLATE = 'plate'
    YEAR = 'year'


class Vehicles(models.Model):
    class Meta():
        ordering = ('-date_of_purchase',)

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
        validators=[MinLengthValidator(17)],
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
        validators=[MinLengthValidator(4), MaxLengthValidator(4)],
        null=False,
        blank=False
    )
    date_of_purchase = models.DateField(
        blank=True,
        null=True
    )
    price = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=0
    )
    # TODO: slug validator
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
    )

    # Auto generate slug
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug:
            self.slug = slugify(f'{self.brand}-{self.plate}')

        return super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('vehicle details', kwargs={'pk': self.pk})

    @property
    def filter_criteries():
        return ('brand', 'model', 'vin', 'plate', 'odometer', 'year', 'date_of_purchase', 'price')

    def __str__(self):
        return self.brand
