from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
from .models import Vehicles
from my_garage.common.middlewares import get_current_request
from django.core.cache import cache
# from cloudinary.uploader import upload, destroy


@receiver(post_save, sender=Vehicles)
def delete_cache(sender, instance, **kwargs):
    cache.delete('service_history')


# @receiver(pre_save, sender=Vehicles)
# def upload_image(sender, instance, **kwargs):
#     request = get_current_request()
#     try:
#         image_file = request.FILES['image_file']
#         upload_result = upload(image_file, folder='vehicles')
#         public_id = upload_result['public_id']
#         image_url = upload_result['secure_url']
#     except:
#         pass


@receiver(pre_delete, sender=Vehicles)
def delete_cache(sender, instance, **kwargs):
    cache.delete('service_history')


# @receiver(pre_delete, sender=Vehicles)
# def delete_image(sender, instance, **kwargs):
#     try:
#         destroy(instance.photo.url)
#     except:
#         pass
