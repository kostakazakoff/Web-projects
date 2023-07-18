from django.shortcuts import render, redirect, resolve_url
from .forms import CreateReminderForm
from .models import Reminder
from django.utils import timezone


def create_reminder_view(request):
    form = CreateReminderForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        reminder = Reminder.objects.latest('pk')
        vehicle_pk = reminder.to_vehicle.pk
        return redirect(resolve_url('garage') + f'#reminder-{vehicle_pk}')

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
        'title': 'Reminders'
    }
    return render(request, 'reminders/reminders.html', context)


def edit_reminder_view(request, pk):
    reminder = Reminder.objects.filter(pk=pk).first()

    context = {
        'reminder': reminder,
    }
    return render(request, 'reminders/edit-reminder.html')


def delete_reminder_view(request, pk):
    reminder = Reminder.objects.filter(pk=pk).first()

    if request.method == 'POST':
        reminder.delete()
        return redirect('reminders')
    
    context = {
        'reminder': reminder,
    }
    return render(request, 'reminders/delete-reminder.html')
