# models.py
from django.db import models
from django.contrib.auth.models import User

class TravelService(models.Model):
    SERVICE_CHOICES = [
        ('bus', 'Bus'),
        ('train', 'Train'),
        ('launch', 'Launch'),
        ('plane', 'Plane'),
        ('hotel', 'Hotel'),
        ('park', 'Park'),
        ('rent', 'Rent')
    ]

    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    from_location = models.CharField(max_length=100)
    to_location = models.CharField(max_length=100)
    journey_date = models.DateField()
    total_seats = models.IntegerField(default=40)  # Default seat count
    available_seats = models.IntegerField(default=40)  # Initially same as total_seats

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_service = models.ForeignKey(TravelService, on_delete=models.CASCADE)
    seats_booked = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    booking_date = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=10,
        choices=[('pending', 'Pending'), ('completed', 'Completed')],
        default='pending'
    )

    def __str__(self):
        return f"{self.user.username} booked {self.seats_booked} seats for {self.travel_service.name}"
