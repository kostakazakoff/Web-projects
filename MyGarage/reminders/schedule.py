from .models import Reminder
from django.utils import timezone
from my_garage.core.utils import send_reminder_email


def check_reminders():
    reminders = Reminder.objects.all()
    have_task_on_odometer = False
    tasks = set()

    for reminder in reminders:
        odometers_to_compare = all([reminder.to_vehicle, reminder.on_odometer])
        
        if odometers_to_compare:
            have_task_on_odometer = reminder.to_vehicle.odometer >= reminder.on_odometer

        if have_task_on_odometer:
            tasks.add(reminder)

        if reminder.on_date and reminder.on_date <= timezone.localdate():
            tasks.add(reminder)

    emails_compose(tasks)


def emails_compose(tasks):
    email_contents = {}

    for task in tasks:
        user = task.to_user
        if user not in email_contents:
            email_contents[user] = []
        email_contents[user].append(task)
    
    for user, details in email_contents.items():
        name = f'{user.profile.first_name}, y' if user.profile.first_name else 'Y'
        message = f'{name}ou\'ve got a tasks:\n'
        message += '\n'.join(f'{m.to_vehicle}: {m.title}' if m.to_vehicle else m.title for m in details)
        send_reminder_email(user, message)