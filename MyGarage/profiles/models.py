from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator, EmailValidator


UserModel = get_user_model()


class Profile(models.Model):
    MAX_NAME_LEN = 30
    MIN_NAME_LEN = 2
    MAX_EMAIL_LEN = 50
    MIN_EMAIL_LEN = 6

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(
            MIN_NAME_LEN,
            f'First name must be at least {MIN_NAME_LEN} characters long'
        )],
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=True,
        blank=True,
        validators=[MinLengthValidator(
            MIN_NAME_LEN,
            f'Last name must be at least {MIN_NAME_LEN} characters long'
        )],
    )

    username = models.CharField(
        blank=False,
        null=False,
        max_length=30,
        unique=True,
        validators=[MinLengthValidator(
            MIN_NAME_LEN,
            f'Username must be at least {MIN_NAME_LEN} characters long')],
    )

    email = models.EmailField(
        max_length=MAX_EMAIL_LEN,
        null=True,
        blank=True,
        unique=True,
        validators=[EmailValidator]
    )

    password = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        validators=[MinLengthValidator(
            MIN_EMAIL_LEN,
            f'Password must be at least {MIN_EMAIL_LEN} characters long'
        )],
    )

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )
