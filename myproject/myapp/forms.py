# forms.py
from django import forms

class SearchForm(forms.Form):
    from_location = forms.CharField(max_length=100, label='Starting Location')
    to_location = forms.CharField(max_length=100, label='Destination')
    journey_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Journey Date')
