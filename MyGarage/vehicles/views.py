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

    # TODO: may insert select menu in vehicle article
    # for vehicle in all_vehicles:
    #     if vehicle.vehicle_service.count() > 0:
    #         for service in vehicle.vehicle_service.all():
    #             service_field.append(
    #                 {'service_id': service.id,
    #                  'vehicle_id': service.vehicle.id,
    #                  'description': service.description,
    #                  'date': service.date.strftime('%Y-%m-%d')}
    #             )
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
    form = CreateVehicleForm(request.POST or None, initial={'default_image': None})
    
    if request.POST.get('submit') == 'save' and form.is_valid():
        form.save()
        return redirect('garage')
    
    if request.POST.get('submit') == 'upload':
        # TODO: upload photo
        return redirect('garage')

    context = {'form': form, 'title': 'Add vehicle'}
    return render(request, 'garage/add-vehicle.html', context)


def edit_vehicle(request, id):
    vehicle = get_object_or_404(Vehicles, pk=id)
    form = CreateVehicleForm(request.POST or None, instance=vehicle)
    print(request.POST.get('submit'))

    if request.POST.get('submit') == 'save' and form.is_valid():
        form.save()
        return redirect('garage')

    if request.POST.get('submit') == 'upload':
        # TODO: upload photo
        return redirect('garage')

    context = {'form': form, 'vehicle': vehicle, 'title': 'Edit vehicle'}
    return render(request, 'garage/edit-vehicle.html', context)


def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicles, pk=id)
    context = {'brand': vehicle.brand}

    if request.method == 'POST':
        if request.POST.get('delete-vehicle'):
            vehicle.delete()
        return redirect('garage')
        
    return render(request, 'garage/delete-vehicle.html', context)
