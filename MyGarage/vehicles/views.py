from django.shortcuts import render
from vehicles.models import Vehicles, Service
from datetime import datetime


def home(request, *args, **kwargs):
    search_str = request.GET.get('header__search_field')
    
    if search_str:
        all_vehicles = Vehicles.objects.filter(brand__icontains=search_str)
    else:
        all_vehicles = Vehicles.objects.all()
        
    context = {'vehicles': all_vehicles, 'title': 'Garage', 'criteria': Vehicles.get_criteria()}
    return render(request, 'home.html', context)


def service(request, *args, **kwargs):
    vehicle_service = [x for x in Service.objects.all().order_by('date')]
    brand = 'All vehicles'

    print(args)
    print(kwargs)

    if kwargs:
        v_id = kwargs['vehicle_id']
        brand = Vehicles.objects.get(id=v_id).brand
        vehicle_service = Service.objects.all().filter(vehicle=v_id).order_by('date')

    context = {
        'service': vehicle_service,
        'title': 'Service History',
        'brand': brand,
        'time': datetime.now()
        }

    return render(request, 'service.html', context)