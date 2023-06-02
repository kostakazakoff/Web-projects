from django.db import models
from photos.validators import validate_img_size_up_to_1mb


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
        upload_to='mediafiles/vehicle_photos/',
        validators=(validate_img_size_up_to_1mb,),
        null=False,
        blank=True,
    )

    def __str__(self):
        return self.name
