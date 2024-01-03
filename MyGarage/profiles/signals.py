from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from my_garage.tasks import send_confirm_registration_email, send_confirm_delete_email
from django.contrib.auth import get_user_model
from .models import Profile


UserModel = get_user_model()


@receiver(post_save, sender=UserModel)
def user_created(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        email = instance.email
        print(email)
        send_confirm_registration_email.delay(email)


@receiver(pre_delete, sender=UserModel)
def delete_media(sender, instance, **kwargs):
    user_reminders = instance.reminder_set.all()
    user_vehicles = instance.vehicles.all()
    for reminder in user_reminders:
        if reminder.photo:
            reminder.photo.delete(save=False)
    for vehicle in user_vehicles:
        if vehicle.photo:
            vehicle.photo.delete(save=False)


@receiver(post_delete, sender=UserModel)
def user_deleted(sender, instance, **kwargs):
    send_confirm_delete_email.delay(instance.email)
