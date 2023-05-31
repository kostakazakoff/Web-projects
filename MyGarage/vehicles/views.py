from django.shortcuts import render, redirect
from vehicles.models import Vehicles, Service
from datetime import datetime


def garage(request, *args, **kwargs):
    search_str = request.GET.get('header__search_field')
    
    if search_str:
        all_vehicles = Vehicles.objects.filter(brand__icontains=search_str) \
        or Vehicles.objects.filter(vin__contains=search_str) \
        or Vehicles.objects.filter(plate__icontains=search_str)
    else:
        all_vehicles = Vehicles.objects.all()
        
    context = {'vehicles': all_vehicles, 'title': 'Garage', 'criteria': Vehicles.get_criteria()}
    return render(request, 'garage/garage.html', context)


def service(request, *args, **kwargs):
    search_str = request.GET.get('header__search_field')
    title = 'All vehicles'

    if kwargs:
        v_id = kwargs['vehicle_id']
        vehicle_service = Service.objects.filter(vehicle=v_id)
        title = vehicle_service.first().vehicle.brand

    if search_str:
        vehicle_service = Service.objects.filter(vehicle__brand__icontains=search_str) \
        or Service.objects.filter(vehicle__vin__contains=search_str) \
        or Service.objects.filter(vehicle__plate__icontains=search_str)
        if vehicle_service:
            print(f'Vehicle service: {vehicle_service}')
            title = vehicle_service.first().vehicle.brand

    if not kwargs and not search_str:
        vehicle_service = [x for x in Service.objects.all()]
    
    context = {
        'service': vehicle_service,
        'title': title,
        'time': datetime.now()
        }

    return render(request, 'service/service.html', context)