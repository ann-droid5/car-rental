from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect, get_object_or_404
from .models import Vehicle, Booking, Customer

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



ADMIN_EMAIL = "admin@cab4cochi.com"
ADMIN_PASSWORD = "admin123"

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'booking/login_error.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        # Create linked Customer
        Customer.objects.create(
            user=user,
            phone=phone
        )

        login(request, user)
        return redirect('/')

    return redirect('/')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # redirect back to same page (modal closes automatically)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('/')

def user_logout(request):
    logout(request)
    return redirect('/')

@login_required
def submit_booking(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle_id')
        pickup = request.POST.get('pickup')
        drop = request.POST.get('drop')
        distance = request.POST.get('distance_km')
        date = request.POST.get('date')
        time = request.POST.get('time')

        customer = Customer.objects.get(user=request.user)
        vehicle = Vehicle.objects.get(id=vehicle_id)

        Booking.objects.create(
            customer=customer,
            vehicle=vehicle,
            pickup_location=pickup,
            drop_location=drop,
            distance_km=distance,
            booking_date=date,
            booking_time=time,
            total_fare=float(distance) * vehicle.price_per_km
        )

        return redirect('/')

def home(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'booking/index.html', {
        'vehicles': vehicles
    })




def adminlogin(request):
    error = None

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
            # mark admin as logged in
            request.session["is_admin"] = True
            return redirect("booking:admindashboard")

        else:
            error = "Invalid admin credentials"

    return render(request, "booking/admin_login.html", {
        "error": error
    })

def admindashboard(request):
    if not request.session.get("is_admin"):
        return redirect("booking:adminlogin")


    return render(request, "booking/admin_dashboard.html")
"""
def adminlogout(request):
    request.session.flush()
    return redirect("adminlogin")"""

def bookingpage(request):
    
    return render(request, 'booking/booking.html')