from typing import Any
from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect, resolve_url
from service.models import Service
from vehicles.models import Vehicles
from django.utils import timezone
from .forms import AddServiceForm
from django.core.cache import cache
from django.views.decorators.cache import cache_page


# @cache_page(30) # Cache timeotut 30 seconds
def search_filter(search_input, pk):

    if not cache.get('service_history'):
        # Caching (<key>, <value>, <timeout>)
        result = cache.set(
            'service_history',
            Service.objects.filter(vehicle=pk),
            24*60*60 # 1 day timeout
            )
    result = cache.get('service_history')

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


def add_service(request, pk):
    vehicle = Vehicles.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = AddServiceForm(request.POST)
        if form.is_valid():
            cache.delete('service_history')
            form.save()
            service_id = Service.objects.latest('pk').id
            return redirect(resolve_url('vehicle service', vehicle.pk) + f'#service-{service_id}')

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


def edit_service(request, service_id):
    service = Service.objects.get(id=service_id)
    vehicle = service.vehicle
    title = 'Edit service'
    form = AddServiceForm(request.POST or None, instance=service)

    if request.method == 'POST':
        if form.is_valid():
            cache.delete('service_history')
            form.save()
            return redirect(resolve_url('vehicle service', vehicle.pk) + f'#service-{service_id}')

    context = {'form': form, 'time': timezone.now(), 'title': title,
               'vehicle': vehicle}

    return render(request, 'service/edit-service.html', context=context)


def delete_service(request, service_id):
    service = Service.objects.get(id=service_id)
    vehicle = service.vehicle

    if request.method == 'POST':
        cache.delete('service_history')
        service.delete()
        return redirect('vehicle service', pk=vehicle.id)

    context = {'vehicle': vehicle}

    return render(request, 'service/delete-service.html', context=context)
