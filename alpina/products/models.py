from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField(max_length=200, blank=False, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=False)
    unit = models.CharField(max_length=10, blank=True, null=True)
    comment = models.TextField(max_length=200, default=None, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('products', kwargs={'id': self.id})


# class Article(models.Model):
#     title = models.CharField(max_length=200, blank=False, null=False)
#     content = 
#     price = models.DecimalField(decimal_places=2, max_digits=1000, blank=True, null=False)
#     comment = models.TextField(max_length=200, default=None, blank=True, null=True)