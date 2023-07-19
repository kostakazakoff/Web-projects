from django.shortcuts import render, redirect, resolve_url

from vehicles.models import Vehicles
from .forms import CreateReminderForm, EditReminderForm
from .models import Reminder
from django.utils import timezone


def create_reminder_view(request):
    form = CreateReminderForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        reminder = Reminder.objects.latest('pk')
        vehicle_pk = reminder.to_vehicle.pk
        return redirect('reminders')
        # return redirect(resolve_url('garage') + f'#vehicle-{vehicle_pk}')

    context = {
        'form': form,
        'title': 'Create Reminder',
        'time': timezone.now(),
    }

    return render(request, 'reminders/create-reminder.html', context)


def search_filter(user, search_input):
    result = Reminder.objects.filter(to_user_id=user.pk)
    nav_search_btn_content = 'fa-solid fa-magnifying-glass'

    if search_input:
        nav_search_btn_content = 'fa-solid fa-arrows-rotate'
        if search_input.isdigit():
            result = result.filter(on_odometer__gte=search_input)
        else:
            vehicle_pk = Vehicles.objects.filter(brand__icontains=search_input).first().pk
            result = result.filter(description__icontains=search_input) or\
                result.filter(title__icontains=search_input) or\
                result.filter(to_vehicle=vehicle_pk)

    return result, nav_search_btn_content


def list_reminders_view(request):
    search_input = request.GET.get('header__search_field', '')

    reminders, nav_search_btn_content = search_filter(
        request.user, search_input
    )

    context = {
        'reminders': reminders,
        'title': 'Reminders',
        'nav_search_btn_content': nav_search_btn_content,
    }
    return render(request, 'reminders/reminders.html', context)


def edit_reminder_view(request, pk):
    reminder = Reminder.objects.filter(pk=pk).first()
    vehicle = reminder.to_vehicle
    form = EditReminderForm(
        request.POST or None,
        request.FILES or None,
        instance=reminder
    )

    if form.is_valid():
        form.save()
        reminder_pk = Reminder.objects.latest('pk').pk
        return redirect(resolve_url('reminders') + f'#reminder-{reminder_pk}')

    context = {
        'form': form,
        'title': f'Edit Reminder for {vehicle}, plate {vehicle.plate}',
        'time': timezone.now(),
        'reminder': reminder,
    }
    return render(request, 'reminders/edit-reminder.html', context)


def delete_reminder_view(request, pk):
    reminder = Reminder.objects.filter(pk=pk).first()

    if request.method == 'POST':
        reminder.delete()
        return redirect('reminders')

    context = {
        'reminder': reminder,
    }
    return render(request, 'reminders/delete-reminder.html', context)
