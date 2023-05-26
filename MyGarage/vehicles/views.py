from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
from vehicles.models import Vehicles, Service
from datetime import datetime


def home(request, *args, **kwargs):
    all_vehicles = Vehicles.objects.all()
    search_str = request.GET.get('header__search_field')

    if search_str:
        all_vehicles = [v for v in all_vehicles if search_str.lower() in v.brand.lower()]
        
    context = {'vehicles': all_vehicles, 'title': 'Garage', 'criteria': Vehicles.get_criteria()}
    return render(request, 'home.html', context)


def service(request, *args, **kwargs):
    vehicle_service = [x for x in Service.objects.all().order_by('date')]
    vehicle = 'All vehicles'

    print(args)
    print(kwargs)

    if kwargs:
        v_id = kwargs['vehicle_id']
        vehicle = next(filter(lambda c: c.id == v_id, Vehicles.objects.all())).brand
        vehicle_service = [x for x in Service.objects.all().order_by('date') if x.vehicle_id == v_id]

    context = {
        'service': vehicle_service,
        'title': 'Service History',
        'vehicle': vehicle,
        'time': datetime.now()
        }

    return render(request, 'service.html', context)