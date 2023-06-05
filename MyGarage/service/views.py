from django.shortcuts import render
from service.models import Service
from datetime import datetime

def vehicle_service_history(request, pk):
    title = 'No service history'
    plate = ''
    search_input = request.GET.get('header__search_field')
    nav_search_btn_content = 'fa-solid fa-magnifying-glass'
    placeholder = 'Autoservice, Description or Odometer'

    vehicle_service = Service.objects.filter(vehicle=pk)
    if vehicle_service:
        title = vehicle_service.first().vehicle.brand
        plate = vehicle_service.first().vehicle.plate

    if search_input:
        nav_search_btn_content = 'fa-solid fa-arrows-rotate'
        if search_input.isdigit():
            vehicle_service = Service.objects.filter(odometer__gte=search_input)
        else:
            vehicle_service = vehicle_service and \
                (Service.objects.filter(autoservice__icontains=search_input) or \
                Service.objects.filter(description__icontains=search_input))
        
        if vehicle_service:
            title = vehicle_service.first().vehicle.brand
            plate = vehicle_service.first().vehicle.plate
    
    context = {
        'service': vehicle_service,
        'title': title,
        'time': datetime.now(),
        'plate': plate,
        'nav_search_btn_content': nav_search_btn_content,
        'placeholder': placeholder
        }

    return render(request, 'service/service.html', context)

def add_service(request):
    return render(request, 'service/add-service.html')

def edit_service(request, service_id):
    return render(request, 'service/edit-service.html')

def delete_service(request, service_id):
    return render(request, 'service/delete-service.html')
