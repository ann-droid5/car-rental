from django.shortcuts import render
from .models import Vehicle


def home(request):
    vehicles = Vehicle.objects.filter(is_available=True)
    return render(request, 'booking/index.html', {
        'vehicles': vehicles
    })

def booking_form(request, vehicle_id):
    vehicle = Vehicle.objects.get(id=vehicle_id)
    return render(request, 'booking/booking_form.html', {
        'vehicle': vehicle
    })