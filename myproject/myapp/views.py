from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, login as auth_login, logout,get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bus,User,BusBooking
#from django.urls import reverse

# Home View

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
        departure_location = request.GET.get('departure_location')
        destination_location = request.GET.get('destination_location')
        journey_date = request.GET.get('journey_date')
        buses = Bus.objects.filter(

            departure_location__icontains= departure_location,
            destination_location__icontains=destination_location,
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


 # Ensures only logged-in users can book
def book_bus(request, bus_id):
    bus = get_object_or_404(Bus, bus_id=bus_id)
    
    if request.method == 'POST':
        # Safely retrieve form values
        passenger_name = request.POST.get('passenger_name', '').strip()
        passenger_phone = request.POST.get('passenger_phone', '').strip()
        selected_seats = request.POST.get('selected_seats', '').strip()
        
        # Validate required fields
        if not passenger_name:
            messages.error(request, "Passenger name is required.")
            return redirect('book_bus', bus_id=bus_id)
        if not passenger_phone:
            messages.error(request, "Passenger phone is required.")
            return redirect('book_bus', bus_id=bus_id)
        if not selected_seats:
            messages.error(request, "Please select the number of seats to book.")
            return redirect('book_bus', bus_id=bus_id)
        
        # Split selected seats
        seat_list = selected_seats.split(',')
        
        # Check if enough seats are available
        if len(seat_list) > bus.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_bus', bus_id=bus_id)
        
        # Calculate total price
        total_price = len(seat_list) * bus.fare
        
        # Resolve SimpleLazyObject to User instance
        #User = get_user_model()  # Ensure compatibility with custom user models
        #current_user = User.objects.get(id=request.user.id)
        
        # Create a new booking and associate it with the logged-in user
        booking = BusBooking(
            #bus=bus,
            passenger_name=passenger_name,
            passenger_phone=passenger_phone,
            selected_seats=selected_seats,
            total_price=total_price,
            #user=current_user,  # Use the resolved User instance
        )
        
        # Update available seats and save booking
        bus.available_seats -= len(seat_list)
        bus.save()
        booking.save()
        
        # Redirect to the payment page
        return redirect('payment_page', booking_id=booking.bus_book_id)
    
    # Render the booking form
    return render(request, 'book_bus.html', {'bus': bus})





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

def book_car(request, rent_id):
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
            return redirect('book_hotel', hotel_id=hotel_id)
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
    #booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'payment.html')

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
