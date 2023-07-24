from datetime import datetime
from django.apps import AppConfig



class RemindersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminders'

    def register_task(self):
        from .tasks import my_scheduled_task
        from background_task.tasks import Task
        print(datetime.datetime.now())
        my_scheduled_task.schedule(repeat=Task.DAILY, time=datetime.time(hour=17, minute=58))

    def ready(self):
        result = super().ready()
        import reminders.signals
        return result
