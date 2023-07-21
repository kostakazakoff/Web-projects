from django.shortcuts import render, redirect, resolve_url
from vehicles.models import Vehicles
from .forms import CreateReminderForm, EditServiceReminderForm, EditReminderForm
from .models import Reminder
from django.utils import timezone
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from my_garage.settings import EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from django.contrib.auth.decorators import login_required

#TODO: send email
def send_email_to_user(request):
    subject = 'Hello from Django!'
    message = 'This is a test email sent using Django.'
    from_email = EMAIL_HOST_USER
    auth_user = EMAIL_HOST_USER
    recipient_list = [request.user.email]
    html_message = '<p>This is the <strong>HTML</strong> version of the email.</p>'

    send_mail(
        subject,
        message,
        from_email,
        recipient_list,
        auth_user,
        # fail_silently=True,
        auth_password=EMAIL_HOST_PASSWORD,
        # html_message=html_message
        )


@login_required
def create_reminder_view(request):
    form = CreateReminderForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        reminder = Reminder.objects.latest('pk')
        return redirect('reminders')

    context = {
        'form': form,
        'title': 'Create Reminder',
        'time': timezone.now(),
    }

    return render(request, 'reminders/create-reminder.html', context)


def search_filter(user, search_input):
    result = Reminder.objects.filter(to_user_id=user.pk)
    nav_search_btn_content = 'fa-solid fa-magnifying-glass'

    if search_input:
        nav_search_btn_content = 'fa-solid fa-arrows-rotate'
        if search_input.isdigit():
            result = result.filter(on_odometer__gte=search_input)
        else:
            vehicle = Vehicles.objects.filter(
                brand__icontains=search_input).first()
            result = result.filter(description__icontains=search_input) or\
                result.filter(title__icontains=search_input) or\
                result.filter(to_vehicle=vehicle)

    return result, nav_search_btn_content


@login_required
def list_reminders_view(request):
    # send_email_to_user(request)
    search_input = request.GET.get('header__search_field', '')

    reminders, nav_search_btn_content = search_filter(
        request.user, search_input
    )

    context = {
        'reminders': reminders,
        'title': 'Reminders',
        'nav_search_btn_content': nav_search_btn_content,
        'placeholder': 'Description, vehicle or odometer'
    }

    return render(request, 'reminders/reminders.html', context)


@login_required
def edit_reminder_view(request, pk):
    reminder = Reminder.objects.filter(pk=pk).first()
    vehicle = reminder.to_vehicle
    title = 'Edit Reminder'
    form = EditReminderForm(
        request.POST or None,
        request.FILES or None,
        instance=reminder
    )

    if vehicle:
        title = f'Edit Reminder for {vehicle} with license plate {vehicle.plate}'
        form = EditServiceReminderForm(
            request.POST or None,
            request.FILES or None,
            instance=reminder
        )

    if form.is_valid():
        form.save()
        reminder_pk = Reminder.objects.latest('pk').pk
        return redirect(resolve_url('reminders') + f'#reminder-{reminder_pk}')

    context = {
        'form': form,
        'title': title,
        'time': timezone.now(),
        'reminder': reminder,
    }
    return render(request, 'reminders/edit-reminder.html', context)


@login_required
def delete_reminder_view(request, pk):
    reminder = Reminder.objects.filter(pk=pk).first()

    if request.method == 'POST':
        reminder.delete()
        return redirect('reminders')

    context = {
        'reminder': reminder,
    }
    return render(request, 'reminders/delete-reminder.html', context)


@login_required
def create_service_reminder(service, user):
    if service.date_deadline or service.odometer_deadline:
        Reminder.objects.create(
            title=service.description,
            description=service.notes,
            on_date=service.date_deadline,
            on_odometer=service.odometer_deadline,
            to_user=user,
            to_vehicle=service.vehicle,
            to_service=service
        )


@login_required
def update_service_reminder(form, reminder):
    reminder.update(
        title=form.cleaned_data['description'],
        description=form.cleaned_data['notes'],
        on_date=form.cleaned_data['date_deadline'],
        on_odometer=form.cleaned_data['odometer_deadline']
    )
