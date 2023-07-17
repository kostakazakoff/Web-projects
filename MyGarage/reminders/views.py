from django.shortcuts import render, redirect
from .forms import CreateServiceReminderForm, CreateReminderForm
from .models import Reminder
from service.models import Service
from django.utils import timezone

# TODO:


def create_service_reminder_view(request, service_pk):
    service = Service.objects.get(pk=service_pk)
    form = CreateServiceReminderForm(
        request.POST or None, initial={
            'title': service.description,
            'description': service.description,
            'to_service': service,
            'on_date': service.date_deadline.strftime('%Y-%m-%d'),
            'on_odometer': service.odometer_deadline
            }
    )

    if form.is_valid():
        form.save()
        return redirect('reminders')

    context = {
        'form': form,
        'title': 'Create Service Reminder',
        'time': timezone.now(),
    }

    return render(request, 'reminders/create-service-reminder.html', context)


def create_reminder_view(request):
    form = CreateReminderForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('reminders')

    context = {
        'form': form,
        'title': 'Create Reminder',
        'time': timezone.now(),
    }

    return render(request, 'reminders/create-reminder.html', context)


def list_reminders_view(request):
    reminders = Reminder.objects.all()
    context = {
        'reminders': reminders,
    }
    return render(request, 'reminders/list-reminders.html', context)


def edit_reminder_view(request, pk):
    return render(request, 'reminders/edit-reminder.html')


def delete_reminder_view(request, pk):
    return render(request, 'reminders/delete-reminder.html')
