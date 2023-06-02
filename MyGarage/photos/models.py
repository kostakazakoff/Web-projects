from django.db import models
from vehicles.models import Vehicles

class Photo(models.Model):
    name = models.CharField(
        max_length=30
        )
    location = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        null=False,
        blank=True,
        default='images/default.jpg',
    )

    def __str__(self):
        return self.name