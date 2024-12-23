from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TravelService, Booking
from django.urls import reverse

# Home View
@login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if password == request.POST['confirm_password']:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            auth_login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')
        else:
            messages.error(request, "Passwords do not match.")
    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

def search_buses(request):
    buses = None
    if request.GET:
        from_location = request.GET.get('from_location')
        to_location = request.GET.get('to_location')
        journey_date = request.GET.get('journey_date')
        buses = TravelService.objects.filter(
            service_type='bus',
            from_location__icontains=from_location,
            to_location__icontains=to_location,
            journey_date=journey_date,
        )
    return render(request, 'search_buses.html', {'buses': buses})     # Copy and adjust for Train , Air, Launch and other. UI will be adjusted later

def car_rental(request):
    cars = None
    if request.GET:
        from_location = request.GET.get('from_location')
        to_location = request.GET.get('to_location')
        journey_date = request.GET.get('journey_date')
        cars = TravelService.objects.filter(
            service_type='rent',
            from_location__icontains=from_location,
            to_location__icontains=to_location,
            journey_date=journey_date,
        )
    return render(request, 'search_buses.html', {'cars': cars})     


@login_required
def book_bus(request, bus_id):
    travel_service = get_object_or_404(TravelService, id=bus_id)
    if request.method == 'POST':
        seats_booked = int(request.POST.get('seats_booked'))
        if seats_booked > travel_service.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_bus', bus_id=bus_id)
        total_price = seats_booked * travel_service.price
        booking = Booking.objects.create(
            travel_service=travel_service,
            user=request.user,
            seats_booked=seats_booked,
            total_price=total_price,
        )
        travel_service.available_seats -= seats_booked
        travel_service.save()
        return redirect('payment_page', booking_id=booking.id)
    return render(request, 'book_bus.html', {'travel_service': travel_service})

def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'payment.html', {'booking': booking})

def confirm_payment(request, booking_id):
    if request.method == "POST":
        booking = get_object_or_404(Booking, id=booking_id)
        booking.payment_status = 'completed'
        booking.save()
        return redirect(reverse('payment_success', args=[booking_id]))
    return redirect('home')

def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'payment_success.html', {'booking': booking})
