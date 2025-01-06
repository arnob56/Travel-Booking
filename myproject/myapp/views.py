from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Bus,User,BusBooking,Air,AirBooking,Train,Launch,Car,Hotel
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm, UserLoginForm , BusForm, PlaneForm, HotelForm, CarForm ,TrainForm, LaunchForm #ParkForm, #EventForm
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
    airs = None
    if request.GET:
        departure_airport = request.GET.get('departure_airport')
        destination_airport = request.GET.get('destination_airport')
        journey_date = request.GET.get('journey_date')
        airs = Air.objects.filter(
            departure_airport__icontains=departure_airport,
            destination_airport__icontains=destination_airport,
            journey_date=journey_date,
        )
    return render(request, 'search_air.html', {'airs': airs}) 

    




def search_trains(request):
    trains = None
    
    if request.GET:
        departure_location = request.GET.get('departure_location')
        destination_location = request.GET.get('destination_location')
        journey_date = request.GET.get('journey_date')
        trains = Train.objects.filter(
            
            departure_location__icontains=departure_location,
            destination_location__icontains=destination_location,
            journey_date=journey_date,
        )
    return render(request, 'search_trains.html', {'trains': trains})




def search_launches(request):

    launches = None
    
    if request.GET:
        departure_location = request.GET.get('departure_location')
        destination_location = request.GET.get('destination_location')
        journey_date = request.GET.get('journey_date')
        launches = Launch.objects.filter(
            
            departure_location__icontains=departure_location,
            destination_location__icontains=destination_location,
            journey_date=journey_date,
        )
    return render(request, 'search_launches.html', {'launches': launches})






def search_cars(request):
    cars = None
    
    if request.GET:
        departure_location = request.GET.get('departure_location')
        destination_location = request.GET.get('destination_location')
        journey_date = request.GET.get('journey_date')
        cars = Car.objects.filter(
            
            departure_location__icontains=departure_location,
            destination_location__icontains=destination_location,
            journey_date=journey_date,
        )
    return render(request, 'search_cars.html', {'cars': cars})  

def hotel_booking(request):


    hotels = None
    
    if request.GET:
        hotel_location=request.GET.get('hotel_location')
        journey_date = request.GET.get('journey_date')
        hotels = Hotel.objects.filter(
            
            hotel_location__icontains=hotel_location,
            journey_date=journey_date,
        )
    return render(request, 'hotel_booking.html', {'hotels': hotels})


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




def book_train(request, train_id):
    train = get_object_or_404(Train, train_id=train_id)
    
    # Prepare the seat grid data
    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    columns = "123456789"
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
            return redirect('book_train', train_id=train_id)
        if not passenger_phone:
            messages.error(request, "Passenger phone is required.")
            return redirect('book_train', train_id=train_id)
        if not selected_seats:
            messages.error(request, "Please select the number of seats to book.")
            return redirect('book_train', train_id=train_id)
        
        # Split selected seats
        seat_list = selected_seats.split(',')
        
        # Check if enough seats are available
        if len(seat_list) > train.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_train', train_id=train_id)
        
        # Calculate total price
        total_price = len(seat_list) * train.fare
        #total_price=total_price,
        
        # Create a new booking and associate it with the logged-in user
        booking = BusBooking(
            
            passenger_name=passenger_name,
            passenger_phone=passenger_phone,
            selected_seats=selected_seats,
            total_price=total_price,
            
        )
        
        # Update available seats and save booking
        train.available_seats -= len(seat_list)
        train.save()
        booking.save()
        
        # Redirect to the payment page
        #return redirect('payment_page', booking_id=booking.bus_book_id)
    
    # Render the booking form with seats data
    return render(request, 'book_train.html', {'train': train, 'seats': seats})

def book_launch(request, launch_id):
    launch = get_object_or_404(Launch, launch_id=launch_id)
    
    # Prepare the seat grid data
    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    columns = "123456789"
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
            return redirect('book_launch', launch_id=launch_id)
        if not passenger_phone:
            messages.error(request, "Passenger phone is required.")
            return redirect('book_launch', launch_id=launch_id)
        if not selected_seats:
            messages.error(request, "Please select the number of seats to book.")
            return redirect('book_launch', launch_id=launch_id)
        
        # Split selected seats
        seat_list = selected_seats.split(',')
        
        # Check if enough seats are available
        if len(seat_list) > launch.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_launch', launch_id=launch_id)
        
        # Calculate total price
        total_price = len(seat_list) * launch.fare
        #total_price=total_price,
        
        # Create a new booking and associate it with the logged-in user
        booking = BusBooking(
            
            passenger_name=passenger_name,
            passenger_phone=passenger_phone,
            selected_seats=selected_seats,
            total_price=total_price,
            
        )
        
        # Update available seats and save booking
        launch.available_seats -= len(seat_list)
        launch.save()
        booking.save()
        
        # Redirect to the payment page
        #return redirect('payment_page', booking_id=booking.bus_book_id)
    
    # Render the booking form with seats data
    return render(request, 'book_launch.html', {'launch':launch, 'seats': seats})

def book_air(request, plane_id):
    plane = get_object_or_404(Air, plane_id=plane_id)
    
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
        if len(seat_list) > plane.available_seats:
            messages.error(request, "Not enough available seats.")
            return redirect('book_air', plane_id=plane_id)
        
        # Calculate total price
        total_price = len(seat_list) * plane.p_fare
        
        # Resolve SimpleLazyObject to User instance
        #User = get_user_model()  # Ensure compatibility with custom user models
        #current_user = User.objects.get(id=request.user.id)
        
        # Create a new booking and associate it with the logged-in user
        p_booking = AirBooking(
            
            passenger_name=passenger_name,
            passenger_phone=passenger_phone,
            selected_seats=selected_seats,
            total_price=total_price,
            #user=current_user,  # Use the resolved User instance
        )
        
        # Update available seats and save booking
        plane.p_available_seats -= len(seat_list)
        plane.save()
        p_booking.save()
        
        # Redirect to the payment page
        
    
    # Render the booking form
    return redirect('book_air', plane_id=plane_id)

def book_car(request, car_id):
    car = get_object_or_404(Car, car_id=car_id)
    if request.method == 'POST':
        # Safely retrieve form values
        passenger_name = request.POST.get('passenger_name', '').strip()
        passenger_phone = request.POST.get('passenger_phone', '').strip()
        selected_seats = request.POST.get('selected_seats', '').strip()
        
        # Validate required fields
        if not passenger_name:
            messages.error(request, "Passenger name is required.")
            return redirect('book_car', car_id=car_id)
        if not passenger_phone:
            messages.error(request, "Passenger phone is required.")
            return redirect('book_car', car_id=car_id)

        
        # Split selected seats

        
        # Calculate total price
        total_price =car.fare
        #total_price=total_price,
        
        # Create a new booking and associate it with the logged-in user
        booking = BusBooking(
            
            passenger_name=passenger_name,
            passenger_phone=passenger_phone,
            selected_seats=selected_seats,
            total_price=total_price,
            
        )
        
        # Update available seats and save booking

        car.save()
        booking.save()
        
        # Redirect to the payment page
        #return redirect('payment_page', booking_id=booking.bus_book_id)
    
    # Render the booking form with seats data
    return render(request, 'book_car.html', {'car':car})


def book_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, hotel_id=hotel_id)
    
    # Prepare the seat grid data
    rows = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    columns = "123456789"
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
            return redirect('book_hotel', hotel_id=hotel_id)
        if not passenger_phone:
            messages.error(request, "Passenger phone is required.")
            return redirect('book_hotel', hotel_id=hotel_id)
        if not selected_seats:
            messages.error(request, "Please select the number of seats to book.")
            return redirect('book_hotel', hotel_id=hotel_id)
        
        # Split selected seats
        seat_list = selected_seats.split(',')
        
        # Check if enough seats are available
        if len(seat_list) > hotel.available_rooms:
            messages.error(request, "Not enough available seats.")
            return redirect('book_bus', hotel_id=hotel_id)
        
        # Calculate total price
        total_price = len(seat_list) * hotel.price
        #total_price=total_price,
        
        # Create a new booking and associate it with the logged-in user
        booking = BusBooking(
            
            passenger_name=passenger_name,
            passenger_phone=passenger_phone,
            selected_seats=selected_seats,
            total_price=total_price,
            
        )
        
        # Update available seats and save booking
        hotel.available_rooms -= len(seat_list)
        hotel.save()
        booking.save()
        
        # Redirect to the payment page
        #return redirect('payment_page', booking_id=booking.bus_book_id)
    
    # Render the booking form with seats data
    return render(request, 'book_hotel.html', {'hotel':hotel, 'seats': seats})



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


def adminn_dashboard(request):
    buses = Bus.objects.all()
    return render(request, 'adminn_dashboard.html', {'buses': buses})

def ad_add_bus(request):
    if request.method == 'POST':
        form = BusForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Bus added successfully!")
            return redirect('adminn_dashboard')
    else:
        form = BusForm()
    return render(request, 'ad_add_bus.html', {'form': form})


def ad_edit_bus(request, bus_id):
    buss = get_object_or_404(Bus, bus_id=bus_id)
    if request.method == 'POST':
        form = BusForm(request.POST, instance=buss)
        if form.is_valid():
            form.save()
            messages.success(request, "Bus updated successfully!")
            return redirect('adminn_dashboard')
    else:
        form = BusForm(instance=bus)
    return render(request, 'ad_edit_bus.html', {'form': form})

def ad_delete_bus(request, bus_id):
    buss = get_object_or_404(Bus, bus_id=bus_id)
    buss.delete()
    messages.success(request, "Bus deleted successfully!")
    return redirect('adminn_dashboard')


def adminn_plane(request):
    airs = Air.objects.all()
    return render(request, 'adminn_plane.html', {'airs': airs})

def ad_add_plane(request):
    if request.method == 'POST':
        form = PlaneForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Plane added successfully!")
            return redirect('adminn_plane')
    else:
        form = PlaneForm()
    return render(request, 'ad_add_plane.html', {'form': form})


def ad_edit_plane(request, plane_id):
    air = get_object_or_404(Air, plane_id=plane_id)
    if request.method == 'POST':
        form = PlaneForm(request.POST, instance=air)
        if form.is_valid():
            form.save()
            messages.success(request, "Plane updated successfully!")
            return redirect('adminn_plane')
    else:
        form = PlaneForm(instance=air)
    return render(request, 'ad_edit_plane.html', {'form': form})


def ad_delete_plane(request, plane_id):
    air = get_object_or_404(Air, plane_id=plane_id)
    air.delete()
    messages.success(request, "Plane deleted successfully!")
    return redirect('adminn_plane')


def adminn_hotel(request):
    hotels = Hotel.objects.all()
    return render(request, 'adminn_hotel.html', {'hotels': hotels})

def ad_add_hotel(request):
    if request.method == 'POST':
        form = HotelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Hotel added successfully!")
            return redirect('adminn_hotel')
    else:
        form = HotelForm()
    return render(request, 'ad_add_hotel.html', {'form': form})


def ad_edit_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, hotel_id=hotel_id)
    if request.method == 'POST':
        form = HotelForm(request.POST, instance=hotel)
        if form.is_valid():
            form.save()
            messages.success(request, "Hotel updated successfully!")
            return redirect('adminn_hotel')
    else:
        form = HotelForm(instance=hotel)
    return render(request, 'ad_edit_hotel.html', {'form': form})


def ad_delete_hotel(request, hotel_id):
    hotel = get_object_or_404(Hotel, hotel_id=hotel_id)
    hotel.delete()
    messages.success(request, "Hotel deleted successfully!")
    return redirect('adminn_hotel')

def adminn_car(request):
    cars = Car.objects.all()
    return render(request, 'adminn_car.html', {'cars': cars})

def ad_add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Car added successfully!")
            return redirect('adminn_car')
    else:
        form = CarForm()
    return render(request, 'ad_add_car.html', {'form': form})


def ad_edit_car(request, car_id):
    car = get_object_or_404(Car, car_id=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            messages.success(request, "Car updated successfully!")
            return redirect('adminn_Car')
    else:
        form = CarForm(instance=car)
    return render(request, 'ad_edit_car.html', {'form': form})


def ad_delete_car(request, car_id):
    car = get_object_or_404(Car, car_id=car_id)
    car.delete()
    messages.success(request, "Car deleted successfully!")
    return redirect('adminn_car')



#Train


def adminn_train(request):
    trains = Train.objects.all()
    return render(request, 'adminn_train.html', {'trains': trains})

def ad_add_train(request):
    if request.method == 'POST':
        form = TrainForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Train has been added successfully!")
            return redirect('adminn_train')
    else:
        form = TrainForm()
    return render(request, 'ad_add_train.html', {'form': form})


def ad_edit_train(request, train_id):
    train = get_object_or_404(Train, train_id=train_id)
    if request.method == 'POST':
        form = TrainForm(request.POST, instance=train)
        if form.is_valid():
            form.save()
            messages.success(request, "Train has been updated successfully!")
            return redirect('adminn_Train')
    else:
        form = TrainForm(instance=train)
    return render(request, 'ad_edit_train.html', {'form': form})


def ad_delete_train(request, train_id):
    train = get_object_or_404(Train, train_id=train_id)
    train.delete()
    messages.success(request, "Train has been deleted successfully!")
    return redirect('adminn_train')



#Launch
def adminn_launch(request):
    launch = Launch.objects.all()
    return render(request, 'adminn_launch.html', {'launch': launch})

def ad_add_launch(request):
    if request.method == 'POST':
        form = LaunchForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Launch has been added successfully!")
            return redirect('adminn_launch')
    else:
        form = LaunchForm()
    return render(request, 'ad_add_launch.html', {'form': form})


def ad_edit_launch(request, launch_id):
    launch = get_object_or_404(Launch, launch_id=launch_id)
    if request.method == 'POST':
        form = LaunchForm(request.POST, instance=launch)
        if form.is_valid():
            form.save()
            messages.success(request, "Launch has been updated successfully!")
            return redirect('adminn_launch')
    else:
        form = LaunchForm(instance=launch)
    return render(request, 'ad_edit_launch.html', {'form': form})


def ad_delete_launch(request, launch_id):
    launch = get_object_or_404(Launch, launch_id=launch_id)
    launch.delete()
    messages.success(request, "Launch has been deleted successfully!")
    return redirect('adminn_launch')



# #Park 

# def adminn_car(request):
#     cars = Car.objects.all()
#     return render(request, 'adminn_car.html', {'cars': cars})

# def ad_add_car(request):
#     if request.method == 'POST':
#         form = CarForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Car added successfully!")
#             return redirect('adminn_car')
#     else:
#         form = CarForm()
#     return render(request, 'ad_add_car.html', {'form': form})


# def ad_edit_car(request, car_id):
#     car = get_object_or_404(Car, car_id=car_id)
#     if request.method == 'POST':
#         form = CarForm(request.POST, instance=car)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Car updated successfully!")
#             return redirect('adminn_Car')
#     else:
#         form = CarForm(instance=car)
#     return render(request, 'ad_edit_car.html', {'form': form})


# def ad_delete_car(request, car_id):
#     car = get_object_or_404(Car, car_id=car_id)
#     car.delete()
#     messages.success(request, "Car deleted successfully!")
#     return redirect('adminn_car')




# #Event


# def adminn_car(request):
#     cars = Car.objects.all()
#     return render(request, 'adminn_car.html', {'cars': cars})

# def ad_add_car(request):
#     if request.method == 'POST':
#         form = CarForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Car added successfully!")
#             return redirect('adminn_car')
#     else:
#         form = CarForm()
#     return render(request, 'ad_add_car.html', {'form': form})


# def ad_edit_car(request, car_id):
#     car = get_object_or_404(Car, car_id=car_id)
#     if request.method == 'POST':
#         form = CarForm(request.POST, instance=car)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Car updated successfully!")
#             return redirect('adminn_Car')
#     else:
#         form = CarForm(instance=car)
#     return render(request, 'ad_edit_car.html', {'form': form})


# def ad_delete_car(request, car_id):
#     car = get_object_or_404(Car, car_id=car_id)
#     car.delete()
#     messages.success(request, "Car deleted successfully!")
#     return redirect('adminn_car')





