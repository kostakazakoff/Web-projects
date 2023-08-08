from django.db.models.signals import pre_save, post_save, m2m_changed
from django.dispatch import receiver
from .models import Service
from my_garage.common.middlewares import get_current_request
from django.contrib.auth import get_user_model
# from django.core.cache import cache


# UserModel = get_user_model()


# @receiver(post_save, sender=Service)
# def delete_cache(sender, instance, **kwargs):
#     cache.delete('service_history')


# @receiver(m2m_changed, sender=Service)
# def delete_cache(sender, instance, **kwargs):
#     cache.delete('service_history')
   