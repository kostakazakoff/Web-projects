from django.core.mail import send_mail
from my_garage.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD


def send_email_to_user(request, subject, message):
    from_email = EMAIL_HOST_USER
    auth_user = EMAIL_HOST_USER
    recipient_list = [request.user.email]
    # html_message = '<p>This is the <strong>HTML</strong> version of the email.</p>'

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        auth_user,
        # fail_silently=True,
        # auth_password=EMAIL_HOST_PASSWORD,
        # html_message=html_message
        )