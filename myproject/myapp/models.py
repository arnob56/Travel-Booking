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
    bus_book_id=models.CharField(max_length=30 ,primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    bus=models.ForeignKey(Bus, on_delete=models.CASCADE)
    passenger_name= models.CharField(max_length=255)
    passenger_phone=models.CharField(max_length=14)
    selected_seats=models.CharField(max_length=200)
    total_price=models.IntegerField(default=0)
    def __str__(self):
        return f"Booking {self.bus_book_id} for {self.user if self.user else self.passenger_name}"

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

    

    

    



    


