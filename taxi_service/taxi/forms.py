from django import forms
from .models import Booking, Driver

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['taxi', 'driver', 'start_datetime', 'end_datetime', 'pickup_location', 'dropoff_location']
        widgets = {
            'start_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'end_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    driver = forms.ModelChoiceField(queryset=Driver.objects.all(), empty_label="Select Driver")