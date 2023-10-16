from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
from reminders.models import Reminder

from reminders.views import create_service_reminder
from .models import Service
from my_garage.common.middlewares import get_current_request
from django.contrib.auth import get_user_model
# from django.core.cache import cache


# UserModel = get_user_model()


@receiver(post_save, sender=Service)
def create_reminder(sender, instance, created, **kwargs):
    if created and (instance.date_deadline or instance.odometer_deadline):
        create_service_reminder(get_current_request(), instance)


# @receiver(post_save, sender=Service)
# def delete_cache(sender, instance, **kwargs):
#     cache.delete('service_history')


# @receiver(m2m_changed, sender=Service)
# def delete_cache(sender, instance, **kwargs):
#     cache.delete('service_history')
   