# forms.p

from django import forms
from .models import User,Bus,Air
from django.contrib.auth.forms import UserCreationForm

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
        
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)


class SearchForm(forms.Form):
    departure_location = forms.CharField(max_length=255, label='Departure Location')
    destination_location = forms.CharField(max_length=255, label='Destination Location')
    journey_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Journey Date')

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = ['bus_id','bus_name', 'bus_description', 'departure_location', 'destination_location','distance','total_time','start_time','arival_time','journey_date','bus_type','total_seats','available_seats','fare']

class PlaneForm(forms.ModelForm):
    class Meta:
        model = Air
        fields = ['plane_id','plane_name', 'plane_description', 'departure_airport', 'destination_airport','total_time','start_time','arival_time','journey_date','p_total_seats','p_available_seats','p_fare']