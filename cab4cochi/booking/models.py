from django.db import models

from django.db import models
from django.contrib.auth.models import User


# -------------------------
# VEHICLE MODEL
# -------------------------
class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('HATCHBACK', 'Hatchback'),
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('TEMPO', 'Tempo Traveller'),
        ('BUS', 'Bus'),
    ]

    name = models.CharField(max_length=50)  
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPES)
    seating_capacity = models.PositiveIntegerField()
    price_per_km = models.DecimalField(max_digits=6, decimal_places=2)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.seating_capacity} seater)"


# -------------------------
# DRIVER MODEL
# -------------------------
class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    license_number = models.CharField(max_length=50)
    has_pcc = models.BooleanField(default=False)  # Police Clearance Certificate
    vehicle = models.OneToOneField(Vehicle, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# -------------------------
# CUSTOMER PROFILE
# -------------------------
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username


# -------------------------
# BOOKING MODEL (CORE)
# -------------------------
class Booking(models.Model):
    BOOKING_STATUS = [
        ('PENDING', 'Pending'),
        ('CONFIRMED', 'Confirmed'),
        ('ON_TRIP', 'On Trip'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True, blank=True)

    pickup_location = models.CharField(max_length=255)
    drop_location = models.CharField(max_length=255)

    distance_km = models.DecimalField(max_digits=6, decimal_places=2)
    total_fare = models.DecimalField(max_digits=8, decimal_places=2)

    booking_date = models.DateField()
    booking_time = models.TimeField()

    status = models.CharField(
        max_length=20,
        choices=BOOKING_STATUS,
        default='PENDING'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer.user.username}"
