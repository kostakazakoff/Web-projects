from django.db import models
from django.urls import reverse


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
    date_of_purchase = models.DateField(
        blank=True,
        null=True
    )
    price = models.IntegerField(
        blank=False,
        null=False,
        default=0
    )
    
    def __str__(self):
        return self.brand
    
    def get_absolute_url(self):
        return reverse('vehicle details', kwargs={'pk': self.pk})
    
    @property
    def filter_criteries():
        return ('brand', 'model', 'vin', 'plate', 'odometer', 'year', 'date_of_purchase', 'price')
    
    
class Service(models.Model):
    class Meta():
        ordering = ('-date',)

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