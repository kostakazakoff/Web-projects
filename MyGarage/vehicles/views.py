# Vehicles
from django.shortcuts import render, redirect, get_object_or_404
from vehicles.models import Vehicles
from .forms import CreateVehicleForm

# TODO: Add dictionaries - currency, language, theme

def garage(request, *args, **kwargs):
    search_input = request.GET.get('header__search_field')
    service_field = []
    nav_search_btn_content = 'fa-solid fa-magnifying-glass'
    placeholder = 'Brand, VIN, Plate or Odometer'
    header_icon_class = 'fa-solid fa-car'

    if search_input:
        nav_search_btn_content = 'fa-solid fa-arrows-rotate'
        if search_input.isdigit():
            all_vehicles = Vehicles.objects.filter(odometer__gte=search_input)
        else: 
            all_vehicles = Vehicles.objects.filter(brand__icontains=search_input) or\
            Vehicles.objects.filter(vin__contains=search_input) or\
            Vehicles.objects.filter(plate__icontains=search_input)
        
    else:
        all_vehicles = Vehicles.objects.all()
        
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
    if request.method == 'POST':
        form = CreateVehicleForm(request.POST, request.FILES)
    
        if form.is_valid():
            form.save()
            v = Vehicles.objects.all().first()
            print(v)
            return redirect('garage')
        
    else:
        form = CreateVehicleForm()

    context = {'form': form, 'title': 'Add vehicle'}
    return render(request, 'garage/add-vehicle.html', context)


def edit_vehicle(request, id):
    vehicle = get_object_or_404(Vehicles, pk=id)

    if request.method == 'POST':
        form = CreateVehicleForm(request.POST, request.FILES, instance=vehicle)
        if request.POST.get('submit') == 'save' and form.is_valid():
            form.save()
            return redirect('garage')
    else:
        form = CreateVehicleForm(instance=vehicle)

    context = {'form': form, 'vehicle': vehicle, 'title': 'Edit vehicle'}
    return render(request, 'garage/edit-vehicle.html', context)


def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicles, pk=id)
    context = {'vehicle': vehicle}

    if request.method == 'POST':
        if request.POST.get('delete-vehicle'):
            vehicle.delete()
        return redirect('garage')
        
    return render(request, 'garage/delete-vehicle.html', context)
