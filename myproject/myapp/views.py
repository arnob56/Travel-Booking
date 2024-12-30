from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bus,User,BusBooking,Air,AirBooking,Train
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm
from .models import User
# Home View

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('search_buses')  
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('search_buses')  
            else:
                form.add_error(None, 'Invalid login credentials')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})



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
        departure_airport = request.GET.get('departure_airport')
        destination_airport = request.GET.get('destination_airport')
        journey_date = request.GET.get('journey_date')
        planes = Air.objects.filter(
            departure_airport__icontains=departure_airport,
            destination_airport__icontains=destination_airport,
            journey_date=journey_date,
        )
    return render(request, 'search_air.html', {'planes': planes}) 

    




# def search_trains(request):
#     trains = None
    
#     if request.GET:
#         from_location = request.GET.get('from_location')
#         to_location = request.GET.get('to_location')
#         journey_date = request.GET.get('journey_date')
#         trains = Train.objects.filter(
            
#             from_location__icontains=from_location,
#             to_location__icontains=to_location,
#             journey_date=journey_date,
#         )
#     return render(request, 'search_trains.html', {'trains': trains})




# def search_launches(request):
#     launches = None
#     if request.GET:
#         from_location = request.GET.get('from_location')
#         to_location = request.GET.get('to_location')
#         journey_date = request.GET.get('journey_date')
#         launches = TravelService.objects.filter(
#             service_type='launch',
#             from_location__icontains=from_location,
#             to_location__icontains=to_location,
#             journey_date=journey_date,
#         )
#     return render(request, 'search_launches.html', {'launches': launches})  






# def car_rentals(request):
#     cars = None
#     if request.GET:
#         from_location = request.GET.get('from_location')
#         to_location = request.GET.get('to_location')
#         journey_date = request.GET.get('journey_date')
#         cars = TravelService.objects.filter(
#             service_type='rent',
#             from_location__icontains=from_location,
#             to_location__icontains=to_location,
#             journey_date=journey_date,
#         )
#     return render(request, 'car_rentals.html', {'cars': cars})    

# def hotel_booking(request):
#     hotels = None
#     if request.GET:
#         to_location = request.GET.get('to_location')
#         journey_date = request.GET.get('journey_date')
#         hotels = TravelService.objects.filter(
#             service_type='hotel',
#             to_location__icontains=to_location,
#             journey_date=journey_date,
#         )
#     return render(request, 'hotel_booking.html', {'hotels': hotels})  


 # Ensures only logged-in users can book

def book_bus(request, bus_id):
    bus = get_object_or_404(Bus, bus_id=bus_id)
    
    # Prepare the seat grid data
    rows = "ABCDEFGHI"
    columns = "1234"
    seats = []

    for row in rows:
        for col in columns:
            seat_number = f"{row}{col}"
            seats.append(seat_number)

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
        #total_price=total_price,
        
        # Create a new booking and associate it with the logged-in user
        booking = BusBooking(
            
            passenger_name=passenger_name,
            passenger_phone=passenger_phone,
            selected_seats=selected_seats,
            total_price=total_price,
            
        )
        
        # Update available seats and save booking
        bus.available_seats -= len(seat_list)
        bus.save()
        booking.save()
        
        # Redirect to the payment page
        #return redirect('payment_page', booking_id=booking.bus_book_id)
    
    # Render the booking form with seats data
    return render(request, 'book_bus.html', {'bus': bus, 'seats': seats})




# def book_train(request, train_id):
#     travel_service = get_object_or_404(TravelService, id=train_id)
#     if request.method == 'POST':
#         seats_booked = int(request.POST.get('seats_booked'))
#         if seats_booked > travel_service.available_seats:
#             messages.error(request, "Not enough available seats.")
#             return redirect('book_train', train_id=train_id)
#         total_price = seats_booked * travel_service.price
#         booking = Booking.objects.create(
#             travel_service=travel_service,
#             user=request.user,
#             seats_booked=seats_booked,
#             total_price=total_price,
#         )
#         travel_service.available_seats -= seats_booked
#         travel_service.save()
#         return redirect('payment_page', booking_id=booking.id)
#     return render(request, 'book_train.html', {'travel_service': travel_service})

# def book_launch(request, launch_id):
#     travel_service = get_object_or_404(TravelService, id=launch_id)
#     if request.method == 'POST':
#         seats_booked = int(request.POST.get('seats_booked'))
#         if seats_booked > travel_service.available_seats:
#             messages.error(request, "Not enough available seats.")
#             return redirect('book_launch', launch_id=launch_id)
#         total_price = seats_booked * travel_service.price
#         booking = Booking.objects.create(
#             travel_service=travel_service,
#             user=request.user,
#             seats_booked=seats_booked,
#             total_price=total_price,
#         )
#         travel_service.available_seats -= seats_booked
#         travel_service.save()
#         return redirect('payment_page', booking_id=booking.id)
#     return render(request, 'book_launch.html', {'travel_service': travel_service})

def book_air(request, plane_id):
    air = get_object_or_404(Air, plane_id=plane_id)
    
    if request.method == 'POST':
        # Safely retrieve form values
        passenger_name = request.POST.get('passenger_name', '').strip()
        passenger_phone = request.POST.get('passenger_phone', '').strip()
        selected_seats = request.POST.get('selected_seats', '').strip()
        
        # Validate required fields
        if not passenger_name:
            messages.error(request, "Passenger name is required.")
            return redirect('book_air', plane_id=plane_id)
        if not passenger_phone:
            messages.error(request, "Passenger phone is required.")
            return redirect('book_air', plane_id=plane_id)
        if not selected_seats:
            messages.error(request, "Please select the number of seats to book.")
            return redirect('book_air', plane_id=plane_id)
        
        # Split selected seats
        seat_list = selected_seats.split(',')
        
        # Check if enough seats are available
        if len(seat_list) > air.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_air', plane_id=plane_id)
        
        # Calculate total price
        total_price = len(seat_list) * air.p_fare
        
        # Resolve SimpleLazyObject to User instance
        #User = get_user_model()  # Ensure compatibility with custom user models
        #current_user = User.objects.get(id=request.user.id)
        
        # Create a new booking and associate it with the logged-in user
        p_booking = AirBooking(
            air=air,
            passenger_name=passenger_name,
            passenger_phone=passenger_phone,
            selected_seats=selected_seats,
            total_price=total_price,
            #user=current_user,  # Use the resolved User instance
        )
        
        # Update available seats and save booking
        air.p_available_seats -= len(seat_list)
        air.save()
        p_booking.save()
        
        # Redirect to the payment page
        return redirect('payment_page', p_booking_id=p_booking.bus_air_id)
    
    # Render the booking form
    return redirect('book_air', plane_id=plane_id)

# def book_car(request, rent_id):
#     travel_service = get_object_or_404(TravelService, id=rent_id)
#     if request.method == 'POST':
#         seats_booked = int(request.POST.get('seats_booked'))
#         if seats_booked > travel_service.available_seats:
#             messages.error(request, "Not enough available seats.")
#             return redirect('book_car', rent_id=rent_id)
#         total_price = seats_booked * travel_service.price
#         booking = Booking.objects.create(
#             travel_service=travel_service,
#             user=request.user,
#             seats_booked=seats_booked,
#             total_price=total_price,
#         )
#         travel_service.available_seats -= seats_booked
#         travel_service.save()
#         return redirect('payment_page', booking_id=booking.id)
#     return render(request, 'book_car.html', {'travel_service': travel_service})


# def book_hotel(request, hotel_id):
#     travel_service = get_object_or_404(TravelService, id=hotel_id)
#     if request.method == 'POST':
#         seats_booked = int(request.POST.get('seats_booked'))
#         if seats_booked > travel_service.available_seats:
#             messages.error(request, "Not enough available seats.")
#             return redirect('book_hotel', hotel_id=hotel_id)
#         total_price = seats_booked * travel_service.price
#         booking = Booking.objects.create(
#             travel_service=travel_service,
#             user=request.user,
#             seats_booked=seats_booked,
#             total_price=total_price,
#         )
#         travel_service.available_seats -= seats_booked
#         travel_service.save()
#         return redirect('payment_page', booking_id=booking.id)
#     return render(request, 'book_hotel.html', {'travel_service': travel_service})



# def payment_page(request, booking_id):
#     #booking = get_object_or_404(Booking, id=booking_id)
#     return render(request, 'payment.html')

# def confirm_payment(request, booking_id):
#     if request.method == "POST":
#         booking = get_object_or_404(Booking, id=booking_id)
#         booking.payment_status = 'completed'
#         booking.save()
#         return redirect(reverse('payment_success', args=[booking_id]))
#     return redirect('home')

# def payment_success(request, booking_id):
#     booking = get_object_or_404(Booking, id=booking_id)
#     return render(request, 'payment_success.html', {'booking': booking})



def payment_page(request):
    booking = get_object_or_404(BusBooking)
    return render(request, 'payment_page.html', {'booking': booking}) 

def ticket_print(request):

    booking = get_object_or_404(BusBooking)

    if booking.payment_status != 'Paid':
        messages.error(request, "Payment is not completed yet.")
        return redirect('payment_page')

    return render(request, 'ticket_print.html', {'booking': booking})


