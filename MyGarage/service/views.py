from django.shortcuts import render
from service.models import Service
from datetime import datetime

def vehicle_service_history(request, *args, **kwargs):
    title = 'No service history'
    search_str = request.GET.get('header__search_field')
    pk = kwargs['pk']

    vehicle_service = Service.objects.filter(vehicle=pk)
    if vehicle_service:
        title = vehicle_service.first().vehicle.brand

    if search_str:
        vehicle_service = vehicle_service and \
            (Service.objects.filter(autoservice__icontains=search_str) or \
            Service.objects.filter(description__icontains=search_str))
        
        if vehicle_service:
            print(f'Vehicle service: {vehicle_service}')
            title = vehicle_service.first().vehicle.brand
    
    context = {
        'service': vehicle_service,
        'title': title,
        'time': datetime.now()
        }

    return render(request, 'service/service.html', context)

def add_service(request):
    pass

def edit_service(request):
    pass

def delete_service(request):
    pass
