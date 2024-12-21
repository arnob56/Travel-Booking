from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TravelService,Booking
from .forms import SearchForm
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
        
        # Validate password match and other conditions
        if password == request.POST['confirm_password']:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()
            
            # After user is saved, authenticate and log the user in
            auth_login(request, user)
            messages.success(request, "Registration successful!")
            return redirect('home')  # Redirect to home or dashboard after successful login
        else:
            messages.error(request, "Passwords do not match.")
    
    return render(request, 'register.html')

# Login User
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('home.html')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'login.html')

# Logout User
def logout_user(request):
    logout(request)
    return redirect('login')


# We'll create this form shortly

def search_buses(request):
    """Search for buses."""
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

@login_required
def book_bus(request, bus_id):
    travel_service = get_object_or_404(TravelService, id=bus_id)

    if request.method == 'POST':
        seats_booked = request.POST.get('seats_booked')
        total_price = int(seats_booked) * travel_service.price
        booking = Booking.objects.create(
            travel_service=travel_service,
            user=request.user,
            seats_booked=seats_booked,
            total_price=total_price,
        )
        # Redirect to the payment page with the booking ID
        return redirect('payment_page', booking_id=booking.id)

    return render(request, 'book_bus.html', {'travel_service': travel_service})



def payment_page(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'payment.html', {'booking': booking})

def confirm_payment(request, booking_id):
    if request.method == "POST":
        booking = get_object_or_404(Booking, id=booking_id)
        # Simulate payment processing here
        booking.payment_status = 'completed'
        booking.save()
        return redirect(reverse('payment_success', args=[booking_id]))
    return redirect('home')

def payment_success(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    return render(request, 'payment_success.html', {'booking': booking})
