# forms.p

from django import forms
from .models import User
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


from .models import Ticket

class TicketForm(forms.ModelForm):
    visit_date = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Ticket
        fields = ['visit_date', 'num_tickets']
