from django.db import models
from my_garage.core.utils import mbytes_to_bytes
from django.core.exceptions import ValidationError
from vehicles.models import Vehicles

#TODO:
'''
Add 'documents' app, OneToMany realated to service (same as 'photos' app)
Remove 'photos' app
'''

class Photo(models.Model):
    MAX_IMG_SIZE = 1.0

    def validate_max_img_size(self):
        if self.file.size > mbytes_to_bytes(Photo.MAX_IMG_SIZE):
            raise ValidationError(f'Max file size is {Photo.MAX_IMG_SIZE}MB')
        
    name = models.CharField(
        max_length=30
    )
    image = models.ImageField(
        upload_to='images',
        validators=(validate_max_img_size,),
        null=False,
        blank=True,
    )
    vehicle = models.ForeignKey(
        Vehicles,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        related_name='uploaded_photos',
        )

    def __str__(self):
        return f'Name={self.name}'
