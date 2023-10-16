from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from my_garage.core.utils import send_confirm_registration_email, send_confirm_delete_email
from django.contrib.auth import get_user_model
from .models import Profile


UserModel = get_user_model()

# TODO: Active users count
@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        send_confirm_registration_email(instance)


#TODO: remove user media files
@receiver(pre_delete, sender=UserModel)
def delete_media(sender, instance, **kwargs):
    pass


@receiver(post_delete, sender=UserModel)
def user_deleted(sender, instance, **kwargs):
    # user_reminders = instance.reminder_set.all()
    # [r.clear_media() for r in user_reminders]
    send_confirm_delete_email(instance)
