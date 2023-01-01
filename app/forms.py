from django import forms
from django.forms import ModelForm, DateInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Custom model imports
from .models import Flight, Hotel

# UserCreationForm is a builtin user register form
class UserEmail(UserCreationForm):
    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class DateInput(forms.DateInput):
    
    input_type = 'date'

### FLIGHT FORM ###
class FlightForm(ModelForm):
    
    flight_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Flight number...'}), label='')
    flight_origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'From (NYC)'}), label='')
    flight_destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'To (ALB)'}), label='')
    flight_gate = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Gate (12A)'}), label='')
    flight_seat = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Seat (3B)'}), label='')
    flight_arrival = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Arrival MM-DD-YYYY'}), label='')
    flight_return = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Return MM-DD-YYYY'}), label='')
    
    class Meta:
        model = Flight
        fields = ('flight_number', 'flight_gate', 'flight_origin', 'flight_destination', 'flight_seat')
        widgets={
            'flight_arrival': DateInput(),
            'flight_return': DateInput()
        }
    
### HOTEL FORM ###
class HotelForm(ModelForm):

    hotel_origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'From (NYC)'}), label='')
    hotel_destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'To (DUB)'}), label='')
    hotel_arrival = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Arrival MM-DD-YYYY'}), label='')
    hotel_return = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Return MM-DD-YYYY'}), label='')
    hotel_travelers = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'# People'}), label='')

    class Meta:
        model = Hotel
        fields = ('hotel_origin', 'hotel_destination', 'hotel_arrival', 'hotel_return', 'hotel_travelers')
        widgets = {
            'hotel_arrival': DateInput(),
            'hotel_return': DateInput()
        }