# Service

from django.db import models
from vehicles.models import Vehicles
from django.urls import reverse


class Service(models.Model):
    class Meta():
        ordering = ('-date',)

    odometer = models.PositiveIntegerField(
        null=False,
        blank=False
        )
    date = models.DateField(
        blank=False,
        null=False,
    )
    description = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    notes = models.TextField(
        # max_length=200,
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
    date_deadline = models.DateField(
        blank=True,
        null=True,
    )
    odometer_deadline = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    # One To Many relations
    vehicle = models.ForeignKey(
        Vehicles,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='vehicle_service',
    )

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse('service details', kwargs={'pk': int(self.pk)})
    
    @property
    def filter_criteries():
        return ('odometer', 'date', 'description', 'notes', 'autoservice', 'price', 'date_deadline', 'odometer_deadline')
