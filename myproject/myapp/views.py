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
    return render(request, 'search_buses.html', {'buses': buses}) 


def search_air(request):
    planes = None
    if request.GET:
        from_location = request.GET.get('from_location')
        to_location = request.GET.get('to_location')
        journey_date = request.GET.get('journey_date')
        planes = TravelService.objects.filter(
            service_type='plane',
            from_location__icontains=from_location,
            to_location__icontains=to_location,
            journey_date=journey_date,
        )
    return render(request, 'search_air.html', {'planes': planes}) 

    




def search_trains(request):
    trains = None
    if request.GET:
        from_location = request.GET.get('from_location')
        to_location = request.GET.get('to_location')
        journey_date = request.GET.get('journey_date')
        trains = TravelService.objects.filter(
            service_type='train',
            from_location__icontains=from_location,
            to_location__icontains=to_location,
            journey_date=journey_date,
        )
    return render(request, 'search_trains.html', {'trains': trains})




def search_launches(request):
    launches = None
    if request.GET:
        from_location = request.GET.get('from_location')
        to_location = request.GET.get('to_location')
        journey_date = request.GET.get('journey_date')
        launches = TravelService.objects.filter(
            service_type='launch',
            from_location__icontains=from_location,
            to_location__icontains=to_location,
            journey_date=journey_date,
        )
    return render(request, 'search_launches.html', {'launches': launches})  






def car_rentals(request):
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
    return render(request, 'car_rentals.html', {'cars': cars})    

def hotel_booking(request):
    hotels = None
    if request.GET:
        to_location = request.GET.get('to_location')
        journey_date = request.GET.get('journey_date')
        hotels = TravelService.objects.filter(
            service_type='hotel',
            to_location__icontains=to_location,
            journey_date=journey_date,
        )
    return render(request, 'hotel_booking.html', {'hotels': hotels})  


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




def book_train(request, train_id):
    travel_service = get_object_or_404(TravelService, id=train_id)
    if request.method == 'POST':
        seats_booked = int(request.POST.get('seats_booked'))
        if seats_booked > travel_service.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_train', train_id=train_id)
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
    return render(request, 'book_train.html', {'travel_service': travel_service})

def book_launch(request, launch_id):
    travel_service = get_object_or_404(TravelService, id=launch_id)
    if request.method == 'POST':
        seats_booked = int(request.POST.get('seats_booked'))
        if seats_booked > travel_service.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_launch', launch_id=launch_id)
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
    return render(request, 'book_launch.html', {'travel_service': travel_service})

def book_air(request, plane_id):
    travel_service = get_object_or_404(TravelService, id=plane_id)
    if request.method == 'POST':
        seats_booked = int(request.POST.get('seats_booked'))
        if seats_booked > travel_service.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_air', plane_id=plane_id)
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
    return render(request, 'book_air.html', {'travel_service': travel_service})

def book_rent(request, rent_id):
    travel_service = get_object_or_404(TravelService, id=rent_id)
    if request.method == 'POST':
        seats_booked = int(request.POST.get('seats_booked'))
        if seats_booked > travel_service.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_car', rent_id=rent_id)
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
    return render(request, 'book_car.html', {'travel_service': travel_service})


def book_hotel(request, hotel_id):
    travel_service = get_object_or_404(TravelService, id=hotel_id)
    if request.method == 'POST':
        seats_booked = int(request.POST.get('seats_booked'))
        if seats_booked > travel_service.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_hotel', rent_id=hotel_id)
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
    return render(request, 'book_hotel.html', {'travel_service': travel_service})



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
