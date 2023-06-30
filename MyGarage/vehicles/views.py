# Vehicles
from django.shortcuts import render, redirect, resolve_url
from vehicles.models import Vehicles
from .forms import CreateVehiclesForm


def search_filter(search_input):
    result = Vehicles.objects.all()
    nav_search_btn_content = 'fa-solid fa-magnifying-glass'

    if search_input:
        nav_search_btn_content = 'fa-solid fa-arrows-rotate'
        
        if search_input.isdigit():
            result = result.filter(odometer__gte=search_input)
        else:
            result = result.filter(brand__icontains=search_input) or\
                result.filter(vin__contains=search_input) or\
                result.filter(plate__icontains=search_input)

    return result, nav_search_btn_content


def garage(request, *args, **kwargs):
    search_input = request.GET.get('header__search_field', '')
    service_field = []
    placeholder = 'Brand, VIN, Plate or Odometer'
    header_icon_class = 'fa-solid fa-car'

    all_vehicles, nav_search_btn_content = search_filter(search_input)

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
        form = CreateVehiclesForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            vehicle_id = Vehicles.objects.latest('pk').id
            return redirect(resolve_url('garage') + f'#vehicle-{vehicle_id}')

    else:
        form = CreateVehiclesForm()

    context = {'form': form, 'title': 'Add vehicle'}
    return render(request, 'garage/add-vehicle.html', context)


def edit_vehicle(request, id):
    vehicle = Vehicles.objects.filter(pk=id).get()

    if request.method == 'POST':
        form = CreateVehiclesForm(
            request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect(resolve_url('garage') + f'#vehicle-{id}')
    else:
        form = CreateVehiclesForm(instance=vehicle)

    context = {'form': form, 'vehicle': vehicle, 'title': 'Edit vehicle'}
    return render(request, 'garage/edit-vehicle.html', context)


def delete_vehicle(request, id):
    vehicle = Vehicles.objects.filter(pk=id).get()
    context = {'vehicle': vehicle}

    if request.method == 'POST':
        if request.POST.get('delete-vehicle'):
            vehicle.delete()
        return redirect('garage')

    return render(request, 'garage/delete-vehicle.html', context)
