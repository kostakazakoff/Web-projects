from django.shortcuts import render
from .forms import CreateReminderForm
from django.utils import timezone


def create_reminder_view(request):
    form = CreateReminderForm(request.POST or None)
    context = {
        'form': form,
        'title': 'Create reminder',
        'time': timezone.now(),
    }
    return render(request, 'reminders/create-reminder.html', context)


def list_reminders_view(request):
    return render(request, 'reminders/list-reminders.html')


def edit_reminder_view(request, pk):
    return render(request, 'reminders/edit-reminder.html')


def delete_reminder_view(request, pk):
    return render(request, 'reminders/delete-reminder.html')
