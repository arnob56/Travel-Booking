# forms.py
from django import forms

class SearchForm(forms.Form):
    departure_location = forms.CharField(max_length=255, label='Departure Location')
    destination_location = forms.CharField(max_length=255, label='Destination Location')
    journey_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Journey Date')
