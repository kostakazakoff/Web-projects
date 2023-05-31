from django.db import models


class Vehicle_choices(models.TextChoices):
    BRAND = 'brand'
    VIN = 'vin'
    PLATE = 'plate'
    YEAR = 'year'


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
        null=False,
        blank=False
        )
    odometer = models.IntegerField(
        null=False,
        blank=False
        )
    year = models.CharField(
        max_length=4,
        null=False,
        blank=False
        )
    
    def __str__(self):
        return self.brand
    
    def get_criteria():
        return ('brand', 'model', 'vin', 'plate', 'odometer', 'year')
    
class Service(models.Model):
    odometer = models.IntegerField(
        null=False,
        blank=False
        )
    date = models.DateField(
        blank=False,
        null=False,
    )
    description = models.TextField(
        blank=False,
        null=False,
        max_length=200
    )
    notes = models.TextField(
        max_length=100,
        null=True,
        blank=True
        )
    autoservice = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        null=False,
        default=0
    )
    vehicle = models.ForeignKey(
        Vehicles,
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    date_deadline = models.DateField(
        blank=True,
        null=True,
    )
    odometer_deadline = models.IntegerField(
        null=True,
        blank=True
    )

    def __str__(self):
        return self.description