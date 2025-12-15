
from django.contrib import admin
from .models import Vehicle, Driver, Customer, Booking


@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'vehicle_type', 'seating_capacity', 'price_per_km', 'is_available')
    list_filter = ('vehicle_type', 'is_available')
    search_fields = ('name',)


@admin.register(Driver)
class DriverAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'license_number', 'has_pcc', 'vehicle')
    list_filter = ('has_pcc',)
    search_fields = ('name', 'phone')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone')
    search_fields = ('user__username', 'phone')


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'customer',
        'vehicle',
        'driver',
        'pickup_location',
        'drop_location',
        'booking_date',
        'status'
    )
    list_filter = ('status', 'booking_date')
    search_fields = ('pickup_location', 'drop_location')
