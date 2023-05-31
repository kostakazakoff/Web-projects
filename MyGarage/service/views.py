from django.shortcuts import render
from service.models import Service
from datetime import datetime

def vehicle_service_history(request, pk):
    title = 'No service history'
    plate = ''
    search_str = request.GET.get('header__search_field')

    vehicle_service = Service.objects.filter(vehicle=pk)
    if vehicle_service:
        title = vehicle_service.first().vehicle.brand
        plate = vehicle_service.first().vehicle.plate

    if search_str:
        vehicle_service = vehicle_service and \
            (Service.objects.filter(autoservice__icontains=search_str) or \
            Service.objects.filter(description__icontains=search_str))
        
        if vehicle_service:
            title = vehicle_service.first().vehicle.brand
            plate = vehicle_service.first().vehicle.plate
    
    context = {
        'service': vehicle_service,
        'title': title,
        'time': datetime.now(),
        'plate': plate,
        }

    return render(request, 'service/service.html', context)

def add_service(request):
    return render(request, 'service/add-service.html')

def edit_service(request, service_id):
    return render(request, 'service/edit-service.html')

def delete_service(request, service_id):
    return render(request, 'service/delete-service.html')
