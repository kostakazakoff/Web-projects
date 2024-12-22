from django.db import models
from django.contrib.auth import models as auth_models
from django.core.validators import MinLengthValidator, EmailValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


class AppUserManager(auth_models.BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        user = self.model(email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_FIELD = 'email'
    objects = AppUserManager()

    email = models.EmailField(
        null=False,
        blank=False,
        unique=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )


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

    created_on = models.DateTimeField(
        auto_now_add=True,
    )

    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        related_name='profile',
        primary_key=True,
    )

    def __str__(self):
        return self.user.email