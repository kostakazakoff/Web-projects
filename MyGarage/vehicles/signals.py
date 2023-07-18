from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Vehicles
from my_garage.common.middlewares import get_current_request
from django.core.cache import cache


@receiver(post_save, sender=Vehicles)
def delete_cache(sender, instance, **kwargs):
    cache.delete('service_history')


@receiver(pre_delete, sender=Vehicles)
def delete_cache(sender, instance, **kwargs):
    cache.delete('service_history')
