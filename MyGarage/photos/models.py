from django.db import models
from my_garage.core.utils import mbytes_to_bytes
from django.core.exceptions import ValidationError

class Photo(models.Model):
    MAX_IMG_SIZE = 1.0

    def validate_max_img_size(self):
        if self.file.size > mbytes_to_bytes(Photo.MAX_IMG_SIZE):
            raise ValidationError(f'Max file size is {Photo.MAX_IMG_SIZE}MB')
        
    name = models.CharField(
        max_length=30
    )
    location = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    image = models.ImageField(
        # upload_to='mediafiles/',
        validators=(validate_max_img_size,),
        null=False,
        blank=True,
    )

    def __str__(self):
        return f'Name={self.name}'
