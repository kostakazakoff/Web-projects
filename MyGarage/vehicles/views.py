from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse, reverse_lazy
from vehicles.models import Vehicles
from .forms import CreateVehiclesForm, UpdateOdometerForm
from django.contrib.auth.decorators import login_required
from django.views import generic as views
from django.contrib.auth.mixins import LoginRequiredMixin
# import cloudinary.api


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
        context['update_odometer_form'] = UpdateOdometerForm()

        return context


# @login_required
# def add_vehicle(request):

#     form = CreateVehiclesForm(request.POST or None, request.FILES or None)
    
#     if form.is_valid():
#         vehicle = form.save(commit=False)
#         vehicle.to_user = request.user
#         vehicle.save()
#         vehicle_id = Vehicles.objects.latest('pk').pk
#         return redirect(resolve_url('garage') + f'#vehicle-{vehicle_id}')

#     context = {'form': form, 'title': 'Add vehicle'}
#     return render(request, 'garage/add-vehicle.html', context)


class AddVehicleView(LoginRequiredMixin, views.View):
    template_name = 'garage/add-vehicle.html'
    form_class = CreateVehiclesForm

    def get(self, request):
        form = self.form_class()
        context = {'form': form, 'title': 'Add vehicle'}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.to_user = request.user
            vehicle.save()
            vehicle_id = Vehicles.objects.latest('pk').pk
            return redirect(resolve_url('garage') + f'#vehicle-{vehicle_id}')

        context = {'form': form, 'title': 'Add vehicle'}
        return render(request, self.template_name, context)


# @login_required
# def edit_vehicle(request, id):
#     vehicle = Vehicles.objects.filter(pk=id).get()

#     form = CreateVehiclesForm(
#         request.POST or None,
#         request.FILES or None,
#         instance=vehicle
#     )

#     if form.is_valid():
#         form.save()
#         return redirect(resolve_url('garage') + f'#vehicle-{id}')

#     context = {'form': form, 'vehicle': vehicle, 'title': 'Edit vehicle'}
#     return render(request, 'garage/edit-vehicle.html', context)


class EditVehicleView(LoginRequiredMixin, views.UpdateView):
    model = Vehicles
    form_class = CreateVehiclesForm
    template_name = 'garage/edit-vehicle.html'
    context_object_name = 'vehicle'

    def get_success_url(self):
        return resolve_url('garage') + f'#vehicle-{self.object.pk}'


# @login_required
# def update_odometer(request, pk=None):
#     direction = request.META['HTTP_REFERER']
#     vehicle = Vehicles.objects.filter(pk=pk).first()
#     if vehicle:
#         form = UpdateOdometerForm(request.POST or None, instance=vehicle)
#         direction = f'{direction}#vehicle-{vehicle.pk}'

#     if form.is_valid():
#         form.save()
        
#     return redirect(direction)
#     # return redirect(resolve_url('garage') + f'#vehicle-{id}')


class UpdateOdometerView(LoginRequiredMixin, views.UpdateView):
    model = Vehicles
    form_class = UpdateOdometerForm
    context_object_name = 'vehicle'
    pk_url_kwarg = 'pk'

    def get_success_url(self):
        direction = self.request.META.get('HTTP_REFERER', '/')
        return f'{direction}#vehicle-{self.object.pk}'


# @login_required
# def delete_vehicle(request, id):
#     vehicle = Vehicles.objects.filter(pk=id).get()
#     context = {'vehicle': vehicle}

#     if request.method == 'POST':
#         vehicle.delete()
#         return redirect('garage')

#     return render(request, 'garage/delete-vehicle.html', context)


class VehicleDeleteView(LoginRequiredMixin, views.DeleteView):
    model = Vehicles
    template_name = 'garage/delete-vehicle.html'
    success_url = reverse_lazy('garage')
    context_object_name = 'vehicle'
