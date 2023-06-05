from django.shortcuts import render
from vehicles.models import Vehicles
from django.shortcuts import get_object_or_404


def garage(request, *args, **kwargs):
    search_str = request.GET.get('header__search_field')
    service_field = []
    nav_search_btn_content = 'fa-solid fa-magnifying-glass'
    placeholder = 'Brand, VIN, Plate or Odometer'
    header_icon_class = 'fa-solid fa-car'

    if search_str:
        nav_search_btn_content = 'fa-solid fa-arrows-rotate'
        all_vehicles = Vehicles.objects.filter(brand__icontains=search_str) or\
        Vehicles.objects.filter(vin__contains=search_str) or\
        Vehicles.objects.filter(plate__icontains=search_str) or \
        Vehicles.objects.filter(odometer__gte=search_str)
    else:
        all_vehicles = Vehicles.objects.all()

    # TODO: may insert select menu in vehicle article
    for vehicle in all_vehicles:
        if vehicle.vehicle_service.count() > 0:
            for service in vehicle.vehicle_service.all():
                service_field.append(
                    {'service_id': service.id,
                     'vehicle_id': service.vehicle.id,
                     'description': service.description,
                     'date': service.date.strftime('%Y-%m-%d')}
                )
    # ------------------------------------------------

    context = {
        'vehicles': all_vehicles,
        'title': 'Garage',
        'vehicles_service': service_field,
        'nav_search_btn_content': nav_search_btn_content,
        'placeholder': placeholder,
        'header_icon_class': header_icon_class
    }
    return render(request, 'garage/garage.html', context)

def add_vehicle(request):
    return render(request, 'garage/add-vehicle.html')


def edit_vehicle(request, id):
    vehicle = get_object_or_404(Vehicles, pk=id)
    context = {'vehicle': vehicle}
    return render(request, 'garage/edit-vehicle.html', context)


def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicles, pk=id)
    context = {'vehicle': vehicle}
    return render(request, 'garage/delete-vehicle.html', context)
