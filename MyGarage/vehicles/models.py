from django.db import models

class Vehicles(models.Model):
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
        null=True,
        blank=True
        )
    plate = models.CharField(
        max_length=10,
        null=True,
        blank=True
        )
    odometer = models.CharField(
        max_length=6,
        null=False,
        blank=False
        )
    year = models.CharField(
        max_length=4,
        null=False,
        blank=False
        )