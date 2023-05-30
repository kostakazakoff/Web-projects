from django.shortcuts import render, redirect
from vehicles.models import Vehicles, Service
from datetime import datetime


def home(request, *args, **kwargs):
    search_str = request.GET.get('header__search_field')
    
    if search_str:
        all_vehicles = Vehicles.objects.filter(brand__icontains=search_str) \
        or Vehicles.objects.filter(vin__contains=search_str) \
        or Vehicles.objects.filter(plate__icontains=search_str)
    else:
        all_vehicles = Vehicles.objects.all()
        
    context = {'vehicles': all_vehicles, 'title': 'Garage', 'criteria': Vehicles.get_criteria()}
    return render(request, 'home.html', context)


def service(request, *args, **kwargs):
    search_str = request.GET.get('header__search_field')

    print(args)
    print(kwargs)

    if kwargs:
        v_id = kwargs['vehicle_id']
        brand = Vehicles.objects.filter(id=v_id).first().brand
        vehicle_service = Service.objects.filter(vehicle=v_id).order_by('date')

    if search_str:
        vehicle_service = Service.objects.filter(vehicle__brand__icontains=search_str).order_by('date') \
        or Service.objects.filter(vehicle__vin__contains=search_str).order_by('date') \
        or Service.objects.filter(vehicle__plate__icontains=search_str).order_by('date')
        brand = vehicle_service.first().vehicle.brand

    if not kwargs and not search_str:
        vehicle_service = [x for x in Service.objects.all().order_by('date')]
        brand = 'All vehicles'
    
    context = {
        'service': vehicle_service,
        'title': 'Service History',
        'brand': brand,
        'time': datetime.now()
        }

    return render(request, 'service.html', context)