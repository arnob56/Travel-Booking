# custom_admin/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import User, Bus, BusBooking

# Dashboard view
def dashboard(request):
    return render(request, 'custom_admin/dashboard.html')

# Manage Users
def manage_users(request):
    users = User.objects.all()
    return render(request, 'custom_admin/manage_users.html', {'users': users})

# Manage Buses
def manage_buses(request):
    buses = Bus.objects.all()
    return render(request, 'custom_admin/manage_buses.html', {'buses': buses})

# Manage Bus Bookings
def manage_bookings(request):
    bookings = BusBooking.objects.all()
    return render(request, 'custom_admin/manage_bookings.html', {'bookings': bookings})
