from django.db import models
from service.models import Service

#TODO: finish the model, migrate
class Reminder(models.Model):
    TITLE_MAX_LEN = 30

    title = models.CharField(
        max_length=TITLE_MAX_LEN,
        null=False,
        blank=False
    )
    description = models.CharField(
        blank=False,
        null=False,
        max_length=100,
    )
    to_service = models.ForeignKey(
        Service,
        null=False,
        blank=False,
        related_name='service_reminders',
        on_delete=models.DO_NOTHING,
    )

    def __str__(self) -> str:
        return self.title
