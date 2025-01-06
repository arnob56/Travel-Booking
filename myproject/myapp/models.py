from django.db import models

class User(models.Model):
    user_id=models.AutoField(primary_key=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    username=models.CharField(max_length=20, unique=True)
    phone=models.CharField(max_length=14, unique=True)
    email=models.CharField(max_length=255 ,unique=True)
    dob=models.DateField()
    gender=models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female')])
    nid=models.CharField(max_length=17,unique=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname} ({self.username}) | Phone: {self.phone}| NID: {self.nid} | Gender: {self.gender} |Date of Birth: {self.dob}"
    

class Bus(models.Model):
    bus_id=models.CharField(max_length=10, primary_key=True)
    bus_name=models.CharField(max_length=255)
    bus_description=models.TextField()
    departure_location=models.CharField(max_length=255)
    destination_location=models.CharField(max_length=255)
    distance=models.FloatField()
    total_time=models.FloatField()
    start_time=models.TimeField()
    arival_time=models.TimeField()
    journey_date=models.DateField()
    bus_type=models.CharField(max_length=10, choices=[('AC', 'AC'), ('Non AC', 'Non AC')])
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    fare=models.IntegerField()

    def __str__(self):
        return f" Bus ID :{self.bus_id} | Bus Name : {self.bus_name} | From : {self.departure_location}  | To: {self.destination_location}  | Bus Type :{self.bus_type}  | Fare :{self.fare}  | Total Seat : {self.total_seats} | Available Seat : {self.available_seats}"
    

class BusBooking(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_phone = models.CharField(max_length=15)
    selected_seats = models.TextField()  # Store selected seats as a string
    total_price = models.IntegerField()
    payment_status = models.CharField(
        max_length=10,
        choices=[('Pending', 'Pending'), ('Paid', 'Paid')],
        default='Paid'
    )  # New field for payment status

    def __str__(self):
        return f" Name: {self.passenger_name}, Price: {self.total_price}, Seats: {self.selected_seats}, Payment: {self.payment_status}"


class TripHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    bus = models.ForeignKey(Bus, on_delete=models.CASCADE)    
    trip_start_time = models.TimeField()
    trip_arrival_time = models.TimeField()
    journey_date = models.DateField()
    seats_booked = models.CharField(max_length=255)  
    total_fare = models.DecimalField(max_digits=10, decimal_places=2)
    #booking_time = models.DateTimeField(auto_now_add=True)  
    status = models.CharField(max_length=20, choices=[('Booked', 'Booked'), ('Completed', 'Completed'), ('Cancelled', 'Cancelled')])

    def __str__(self):
        return f"Trip from {self.bus.from_city} to {self.bus.to_city} on {self.journey_date} - {self.status}"
    
class Air(models.Model):
    plane_id=models.CharField(max_length=10, primary_key=True)
    plane_name=models.CharField(max_length=255)
    plane_description=models.TextField()
    departure_airport=models.CharField(max_length=255)
    destination_airport=models.CharField(max_length=255)
    total_time=models.FloatField()
    start_time=models.TimeField()
    arival_time=models.TimeField()
    journey_date=models.DateField()
    #class_type=models.CharField(max_length=10, choices=[('Economy', 'Economy'), ('Business Class', 'Business Class')])
    p_total_seats=models.IntegerField()
    p_available_seats=models.IntegerField()
    p_fare=models.IntegerField()

    def __str__(self):
        return f" Plane ID :{self.plane_id} | Plane Name : {self.plane_name} | From : {self.departure_airport}  | To: {self.destination_airport} | Fare :{self.p_fare}  | Total Seat : {self.p_total_seats} | Available Seat : {self.p_available_seats}"
    

class AirBooking(models.Model):
    plane_book_id=models.CharField(max_length=30 ,primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    air=models.ForeignKey(Air, on_delete=models.CASCADE)
    passenger_name= models.CharField(max_length=255)
    passenger_phone=models.CharField(max_length=14)
    selected_seats=models.CharField(max_length=200)
    total_price=models.IntegerField(default=0)
    def __str__(self):
        return f"Booking {self.plane_book_id} for {self.user if self.user else self.passenger_name}"

    def get_selected_seats_list(self):
        
        return list(map(int, self.selected_seats.split(',')))

    def add_seat(self, seat_number):
        
        seat_list = self.get_selected_seats_list()
        if seat_number not in seat_list:
            seat_list.append(seat_number)
            self.selected_seats = ','.join(map(str, seat_list))
            self.save()

    def remove_seat(self, seat_number):
        
        seat_list = self.get_selected_seats_list()
        if seat_number in seat_list:
            seat_list.remove(seat_number)
            self.selected_seats = ','.join(map(str, seat_list))
            self.save()

class Train(models.Model):
    train_id=models.CharField(max_length=10, primary_key=True)
    train_name=models.CharField(max_length=255)
    departure_location=models.CharField(max_length=255)
    destination_location=models.CharField(max_length=255)
    start_time=models.TimeField()
    arival_time=models.TimeField()
    journey_date=models.DateField()
    #bus_type=models.CharField(max_length=10, choices=[('AC', 'AC'), ('Non AC', 'Non AC')])
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    fare=models.IntegerField()

    def __str__(self):
        return f" Train ID :{self.train_id} | Bus Name : {self.train_name} | From : {self.departure_location}  | To: {self.destination_location}  | | Fare :{self.fare}  | Total Seat : {self.total_seats} | Available Seat : {self.available_seats}"

class TrainBooking(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_phone = models.CharField(max_length=15)
    selected_seats = models.TextField()  # Store selected seats as a string

    def __str__(self):
        return {self.passenger_name}
    
class Launch(models.Model):
    launch_id=models.CharField(max_length=10, primary_key=True)
    launch_name=models.CharField(max_length=255)
    departure_location=models.CharField(max_length=255)
    destination_location=models.CharField(max_length=255)
    start_time=models.TimeField()
    arival_time=models.TimeField()
    journey_date=models.DateField()
    #bus_type=models.CharField(max_length=10, choices=[('AC', 'AC'), ('Non AC', 'Non AC')])
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    fare=models.IntegerField()

    def __str__(self):
        return f" Launch ID :{self.launch_id} | Bus Name : {self.launch_name} | From : {self.departure_location}  | To: {self.destination_location}  | | Fare :{self.fare}  | Total Seat : {self.total_seats} | Available Seat : {self.available_seats}"

    
class Hotel(models.Model):
    hotel_id=models.CharField(max_length=10, primary_key=True)
    hotel_name=models.CharField(max_length=255)
    hotel_location=models.CharField(max_length=255)

    journey_date=models.DateField()
    #bus_type=models.CharField(max_length=10, choices=[('AC', 'AC'), ('Non AC', 'Non AC')])
    total_rooms=models.IntegerField()
    available_rooms=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return f" Hotel ID :{self.hotel_id} | Hotel Name : {self.hotel_name} | Location : {self.hotel_location} | | Price :{self.price}  | Total room : {self.total_rooms} | Available Rooms : {self.available_rooms}"
    
class Car(models.Model):
    car_id=models.CharField(max_length=10, primary_key=True)
    car_serial=models.CharField(max_length=255)
    car_name=models.CharField(max_length=255)
    departure_location=models.CharField(max_length=255)
    destination_location=models.CharField(max_length=255)
    time=models.TimeField()

    journey_date=models.DateField()

    fare=models.IntegerField()


    def __str__(self):
        return (
    f"Car Serial: {self.car_serial} | "
    f"Car Name: {self.car_name} | "
    f"From Location: {self.departure_location} | "
    f"To Location: {self.destination_location} || "
    f"Price: {self.fare}"
)
# class Park(models.Model):
#     park_id=models.CharField(max_length=10, primary_key=True)
#     park_name=models.CharField(max_length=255)
#     park_location=models.CharField(max_length=255)

#     date=models.DateField()
#     #bus_type=models.CharField(max_length=10, choices=[('AC', 'AC'), ('Non AC', 'Non AC')])
#     total_rooms=models.IntegerField()
#     available_rooms=models.IntegerField()
#     fare=models.IntegerField()

#     def __str__(self):
#         return f" Park Name :{self.park_name} Park Location: {self.park_location}"
    
class Events(models.Model):
    event_id=models.CharField(max_length=10, primary_key=True)
    event_name=models.CharField(max_length=255)
    event_location=models.CharField(max_length=255)

    event_date=models.DateField()
    event_type=models.CharField(max_length=10, choices=[('BPL', 'BPL'), ('Movie', 'Movie')])
    total_seats=models.IntegerField()
    available_seats=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return f" Hotel ID :{self.event_id} | Hotel Name : {self.event_name} | Location : {self.event_location} | | Price :{self.price}"


class Park(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    entry_fee = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

class Ticket(models.Model):
    park = models.ForeignKey(Park, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(auto_now_add=True)
    visit_date = models.DateField()
    num_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.username} - {self.park.name}"
