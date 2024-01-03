from celery import shared_task
from django.core.mail import send_mail
from my_garage.settings import EMAIL_HOST_USER
from django.template.loader import render_to_string

@shared_task
def send_confirm_registration_email(user):
    subject = 'Account confirmation'
    message = 'Your account was created successfully. You may change your proile details in app menu - USER/EDIT PROFILE'
    from_email = EMAIL_HOST_USER
    recipient_list = [user.email]
    context={'user': user.email}
    html_message = render_to_string('emails/register-confirmation.html', context=context)

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        # fail_silently=True,
        # auth_password=EMAIL_HOST_PASSWORD,
        html_message=html_message,
    )

@shared_task
def send_confirm_delete_email(user):
    subject = 'User deletion confirmation'
    message = 'Your account was deleted successfully.'
    from_email = EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
    )

@shared_task
def send_reminder_email(user, message):
    subject = 'Reminder'
    from_email = EMAIL_HOST_USER
    recipient_list = [user.email]

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
    )
