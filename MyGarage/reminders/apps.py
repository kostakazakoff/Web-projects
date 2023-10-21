from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


# TODO: Transform scheduling into Celery & Redis
class RemindersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminders'

    def ready(self):
        result = super().ready()
        import reminders.signals # must import signals manualy (signals are not a part of Django convension)
        from .schedule import check_reminders
        scheduler = BackgroundScheduler()
        scheduler.add_job(check_reminders, 'cron', hour=13, minute=22)
        scheduler.start()
        return result
