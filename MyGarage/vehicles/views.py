from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import JsonResponse
from vehicles.models import Vehicles, Service


def index(request, *args, **kwargs):
    all_vehicles = Vehicles.objects.all()
    context = {'vehicles': all_vehicles, 'title': 'Garage'}

    return render(request, 'index.html', context)

def service(request, *args, **kwargs):
    print(f'Args: {args}')
    print(f'Kwargs: {kwargs}')

    vehicle_service = [x for x in Service.objects.all().order_by('date')]
    car = 'All vehicles'

    if kwargs:
        v_id = kwargs['vehicle_id']
        car = next(filter(lambda c: c.id == v_id, Vehicles.objects.all())).brand
        vehicle_service = [x for x in Service.objects.all().order_by('date') if x.vehicle_id == v_id]

    context = {'service': vehicle_service, 'title': 'Service', 'vehicle': car}

    return render(request, 'service.html', context)