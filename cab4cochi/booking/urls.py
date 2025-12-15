from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/<int:vehicle_id>/', views.booking_form, name='booking_form'),
]
