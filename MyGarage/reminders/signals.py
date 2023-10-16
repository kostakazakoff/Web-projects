from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Reminder
from my_garage.common.middlewares import get_current_request


@receiver(pre_save, sender=Reminder)
def attach_user_to_reminder(sender, instance, **kwargs):
    instance.to_user = get_current_request().user

@receiver(pre_save, sender=Reminder)
def set_reminder_photo(sender, instance, **kwargs):
    if instance.to_vehicle.photo:
        instance.photo = instance.to_vehicle.photo