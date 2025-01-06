# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Bus, Air, Event, Park, ParkTicket

# User Registration Form (same as before)
class UserRegisterForm(UserCreationForm):
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=14)
    email = forms.EmailField(max_length=255)
    dob = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, 2024)))
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    nid = forms.CharField(max_length=17)

    class Meta:
        model = User
        fields = ['firstname', 'lastname', 'username', 'phone', 'email', 'dob', 'gender', 'nid', 'password1', 'password2']

# Bus Ticket Booking Form
class BusTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['bus', 'num_tickets']

# Air Ticket Booking Form
class AirTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['air', 'num_tickets']

# Event Ticket Booking Form
class EventTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['event', 'num_tickets']

# Park Ticket Booking Form (added)
class ParkTicketForm(forms.ModelForm):
    class Meta:
        model = ParkTicket
        fields = ['park', 'num_tickets', 'visit_date']
