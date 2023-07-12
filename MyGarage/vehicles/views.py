from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse, reverse_lazy
from vehicles.models import Vehicles
from .forms import CreateVehiclesForm
from django.contrib.auth.decorators import login_required
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin

# TODO: Change odometer view


class GarageView(LoginRequiredMixin, views.ListView):
    template_name = 'garage/garage.html'
    model = Vehicles
    context_object_name = 'vehicles'

    def get_queryset(self):
        search_input = self.request.GET.get('header__search_field', '')
        queryset = super().get_queryset()
        queryset = queryset.filter(to_user=self.request.user)

        if search_input:
            if search_input.isdigit():
                queryset = queryset.filter(odometer__gte=search_input)
            else:
                queryset = queryset.filter(brand__icontains=search_input) or\
                    queryset.filter(vin__contains=search_input) or\
                    queryset.filter(plate__icontains=search_input)

        return queryset

    def get_context_data(self, **kwargs):
        search_input = self.request.GET.get('header__search_field', '')
        nav_search_btn_content = 'fa-solid fa-magnifying-glass'
        context = super().get_context_data(**kwargs)

        if search_input:
            nav_search_btn_content = 'fa-solid fa-arrows-rotate'

        context['all_vehicles'] = self.object_list
        context['nav_search_btn_content'] = nav_search_btn_content
        context['title'] = 'Garage'
        context['placeholder'] = 'Brand, VIN, Plate or Odometer'

        return context


@login_required
def add_vehicle(request):

    form = CreateVehiclesForm(request.POST or None, request.FILES or None)
    vehicle = form.save(commit=False)
    vehicle.to_user = request.user

    if form.is_valid():
        form.save()
        vehicle_id = Vehicles.objects.latest('pk').pk
        return redirect(resolve_url('garage') + f'#vehicle-{vehicle_id}')

    context = {'form': form, 'title': 'Add vehicle'}
    return render(request, 'garage/add-vehicle.html', context)


@login_required
def edit_vehicle(request, id):
    vehicle = Vehicles.objects.filter(pk=id).get()

    form = CreateVehiclesForm(
        request.POST or None,
        request.FILES or None,
        instance=vehicle
    )

    if form.is_valid():
        form.save()
        return redirect(resolve_url('garage') + f'#vehicle-{id}')

    context = {'form': form, 'vehicle': vehicle, 'title': 'Edit vehicle'}
    return render(request, 'garage/edit-vehicle.html', context)


@login_required
def delete_vehicle(request, id):
    vehicle = Vehicles.objects.filter(pk=id).get()
    context = {'vehicle': vehicle}

    if request.method == 'POST':
        vehicle.delete()
        return redirect('garage')

    return render(request, 'garage/delete-vehicle.html', context)


# def search_filter(user, search_input):
#     result = Vehicles.objects.filter(to_user_id=user.pk)
#     nav_search_btn_content = 'fa-solid fa-magnifying-glass'

#     if search_input:
#         nav_search_btn_content = 'fa-solid fa-arrows-rotate'

#         if search_input.isdigit():
#             result = result.filter(odometer__gte=search_input)
#         else:
#             result = result.filter(brand__icontains=search_input) or\
#                 result.filter(vin__contains=search_input) or\
#                 result.filter(plate__icontains=search_input)

#     return result, nav_search_btn_content


# def garage(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect('sign in')

#     search_input = request.GET.get('header__search_field', '')
#     service_field = []
#     placeholder = 'Brand, VIN, Plate or Odometer'
#     header_icon_class = 'fa-solid fa-car'

#     all_vehicles, nav_search_btn_content = search_filter(request.user, search_input)

#     context = {
#         'vehicles': all_vehicles,
#         'title': 'Garage',
#         'vehicles_service': service_field,
#         'nav_search_btn_content': nav_search_btn_content,
#         'placeholder': placeholder,
#         'header_icon_class': header_icon_class
#     }
#     return render(request, 'garage/garage.html', context)
