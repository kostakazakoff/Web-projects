from django.db import models
from service.models import Service
from django.contrib.auth import get_user_model

#TODO: validators
UserModel = get_user_model()


class Reminder(models.Model):
    TITLE_MAX_LEN = 30
    DESCRIPTION_MAX_LEN = 100

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False
    )
    description = models.CharField(
        blank=True,
        null=True,
        max_length=DESCRIPTION_MAX_LEN,
    )
    #TODO:
    recurs = models.DateField(
        null=True,
        blank=True,
    )
    to_user = models.ForeignKey(
        UserModel,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
    )
    done = models.BooleanField(
        null=False,
        blank=True,
        default=False,
    )

    def __str__(self) -> str:
        return self.title
