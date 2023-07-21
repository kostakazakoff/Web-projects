from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, resolve_url
from service.models import Service
from reminders.models import Reminder
from vehicles.models import Vehicles
from django.utils import timezone
from .forms import AddServiceForm
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from reminders.views import create_service_reminder, update_service_reminder
from django.contrib.auth.decorators import login_required


# @cache_page(30) # Cache timeotut 30 seconds
def search_filter(search_input, pk):

    # if not cache.get('service_history'):
    #     # Caching (<key>, <value>, <timeout>)
    #     result = cache.set(
    #         'service_history',
    #         Service.objects.filter(vehicle=pk),
    #         24*60*60 # 1 day timeout
    #         )
    # result = cache.get('service_history')

    # No cache result:
    result = Service.objects.filter(vehicle=pk)

    nav_search_btn_content = 'fa-solid fa-magnifying-glass'

    if search_input != '':
        nav_search_btn_content = 'fa-solid fa-arrows-rotate'

        if search_input.isdigit():
            result = result.filter(odometer__gte=search_input)
        else:
            result = result.filter(autoservice__icontains=search_input) or \
                result.filter(description__icontains=search_input) or \
                result.filter(notes__icontains=search_input)

    return result, nav_search_btn_content


def vehicle_service_history(request, pk):
    vehicle = Vehicles.objects.get(pk=pk)
    title = f'{vehicle.brand} {vehicle.plate} | Odometer: {vehicle.odometer}'
    search_input = request.GET.get('header__search_field', '')
    placeholder = 'Autoservice, Description or Odometer'

    vehicle_service, nav_search_btn_content = search_filter(search_input, pk)

    context = {
        'service': vehicle_service,
        'title': title,
        'date': timezone.localdate(),
        'nav_search_btn_content': nav_search_btn_content,
        'placeholder': placeholder,
        'vehicle': vehicle,
        'search': search_input,
    }

    return render(request, 'service/service.html', context)


@login_required
def add_service(request, pk):
    vehicle = Vehicles.objects.get(pk=pk)

    if request.method == 'POST':
        form = AddServiceForm(request.POST)
        if form.is_valid():
            # cache.delete('service_history')
            form.save()
            service = Service.objects.latest('pk')
            create_service_reminder(request, service)
            return redirect(resolve_url('vehicle service', vehicle.pk) + f'#service-{service.id}')

    elif request.method == 'GET':
        form = AddServiceForm(initial={
            'vehicle': pk,
            'date': timezone.now(),
            'odometer': vehicle.odometer
        })

    context = {
        'title': 'Add service',
        'pk': pk,
        'time': timezone.now(),
        'form': form,
        'vehicle': vehicle,
    }
    return render(request, 'service/add-service.html', context)


@login_required
def edit_service(request, service_id):
    service = Service.objects.get(id=service_id)
    vehicle = service.vehicle
    title = 'Edit service'
    form = AddServiceForm(request.POST or None, instance=service)

    if request.method == 'POST':
        if form.is_valid():
            # cache.delete('service_history')
            service_reminder = service.reminder_set.all().first()
            data_for_remind = any([
                form.cleaned_data['date_deadline'],
                form.cleaned_data['odometer_deadline'],
            ])
            have_to_create_reminder = all(
                [
                    not service_reminder,
                    form.has_changed(),
                    data_for_remind
                ]
            )

            if service_reminder:
                # service_reminder = service_reminder.filter(
                #     title=form.cleaned_data['description']).first()

                have_to_update_reminder = all(
                    [
                        service_reminder,
                        form.has_changed(),
                    ]
                )
                have_to_create_reminder = all(
                    [
                        not service_reminder,
                        form.has_changed(),
                        data_for_remind
                    ]
                )
                have_to_delete_reminder = all([
                    service_reminder,
                    not data_for_remind
                ])

                if have_to_update_reminder:
                    print('have to update reminder')
                    obj = Reminder.objects.filter(pk=service_reminder.pk)
                    update_service_reminder(form, obj)

                if have_to_delete_reminder:
                    obj = Reminder.objects.filter(pk=service_reminder.pk)
                    obj.delete()

            if have_to_create_reminder:
                print('have to create reminder')
                create_service_reminder(request, service)

            form.save()
            return redirect(resolve_url('vehicle service', vehicle.pk) + f'#service-{service_id}')

    context = {'form': form, 'time': timezone.now(), 'title': title,
               'vehicle': vehicle}

    return render(request, 'service/edit-service.html', context=context)


@login_required
def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)
    vehicle = service.vehicle

    if request.method == 'POST':
        cache.delete('service_history')
        service.delete()
        return redirect('vehicle service', pk=vehicle.id)

    context = {'vehicle': vehicle}

    return render(request, 'service/delete-service.html', context=context)
