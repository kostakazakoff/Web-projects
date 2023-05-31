from django.shortcuts import render, redirect
from vehicles.models import Vehicles


def garage(request, *args, **kwargs):
    search_str = request.GET.get('header__search_field')
    
    if search_str:
        all_vehicles = Vehicles.objects.filter(brand__icontains=search_str) \
        or Vehicles.objects.filter(vin__contains=search_str) \
        or Vehicles.objects.filter(plate__icontains=search_str)
    else:
        all_vehicles = Vehicles.objects.all()
        
    context = {'vehicles': all_vehicles, 'title': 'Garage'}
    return render(request, 'garage/garage.html', context)
