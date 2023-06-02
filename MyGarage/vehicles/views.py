from django.shortcuts import render
from vehicles.models import Vehicles
from django.shortcuts import get_object_or_404


def garage(request, *args, **kwargs):
    search_str = request.GET.get('header__search_field')
    
    if search_str:
        all_vehicles = Vehicles.objects.filter(brand__icontains=search_str) \
        or Vehicles.objects.filter(vin__contains=search_str) \
        or Vehicles.objects.filter(plate__icontains=search_str)
    else:
        all_vehicles = Vehicles.objects.all()
        
    context = {
        'vehicles': all_vehicles,
        'title': 'Garage'
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