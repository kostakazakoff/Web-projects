from django.db import models, router
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth import get_user_model
from my_garage.core.validators import (
    value_is_17_chars,
    year_is_valid,
    validate_max_date,
)
from django.db.models.deletion import Collector
# from cloudinary_storage.storage import MediaCloudinaryStorage
# import cloudinary.api
# from cloudinary.uploader import upload, destroy


UserModel = get_user_model()


class Vehicles(models.Model):
    BRAND_MODEL_MAX_LEN = 30
    VIN_LEN = 17
    PLATE_LEN = 10
    YEAR_LEN = 4

    class Meta:
        ordering = ('-year',)

    brand = models.CharField(
        max_length=BRAND_MODEL_MAX_LEN,
        null=False,
        blank=False
    )
    model = models.CharField(
        max_length=BRAND_MODEL_MAX_LEN,
        null=True,
        blank=True
    )
    vin = models.CharField(
        max_length=VIN_LEN,
        validators=[value_is_17_chars],
        null=True,
        blank=True,
        unique=True,
    )
    plate = models.CharField(
        max_length=PLATE_LEN,
        null=False,
        blank=False,
        unique=True,
    )
    odometer = models.PositiveIntegerField(
        null=False,
        blank=False
    )
    year = models.CharField(
        max_length=YEAR_LEN,
        validators=[year_is_valid],
        null=False,
        blank=False
    )
    date_of_purchase = models.DateField(
        blank=True,
        null=True,
        validators=[validate_max_date],
    )
    price = models.PositiveIntegerField(
        blank=False,
        null=False,
        default=0,
    )
    photo = models.ImageField(
        upload_to='vehicles/',
        # storage=MediaCloudinaryStorage(),
        blank=True,
        null=True,
    )
    
    slug = models.SlugField(
        unique=True,
        null=False,
        blank=True,
        editable=False,
    )

    to_user = models.ForeignKey(
        UserModel,
        null=False,
        blank=True,
        on_delete=models.CASCADE,
        related_name='vehicles',
        editable=False,
    )

    def save(self, *args, **kwargs):
        # Delete old image file from cloud if exist
        try:
            current = Vehicles.objects.get(id=self.id)
            if not self.photo or current.photo.url != self.photo.url:
                # destroy(str(current.photo))
                current.photo.delete()
        except:
            pass

        # Auto generate slug
        if not self.slug:
            self.slug = slugify(f'{self.brand}-{self.plate}')

        super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        if self.photo:
            # destroy(str(self.photo))
            self.photo.delete()

        super().delete(*args, **kwargs)

    # def get_absolute_url(self):
    #     return reverse('vehicle details', kwargs={'pk': self.pk})

    def __str__(self):
        return f'{self.brand} {self.model}'
