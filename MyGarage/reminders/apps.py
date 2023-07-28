from django.apps import AppConfig
from apscheduler.schedulers.background import BackgroundScheduler


class RemindersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminders'

    def ready(self):
        result = super().ready()
        import reminders.signals
        from .schedule import check_reminders
        scheduler = BackgroundScheduler()
        scheduler.add_job(check_reminders, 'cron', hour=22, minute=6)
        scheduler.start()
        return result
