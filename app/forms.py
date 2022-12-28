from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Custom model imports
from .models import Flight


class UserEmail(UserCreationForm):
    
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class DateInput(forms.DateInput):
    
    input_type = 'date'

class FlightForm(ModelForm):
    
    flight_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Flight number...'}), label='')
    flight_origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'From (NYC)'}), label='')
    flight_destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'To (ALB)'}), label='')
    flight_arrival = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Arrival MM-DD-YYYY'}), label='')
    flight_return = forms.DateField(widget=forms.TextInput(attrs={'placeholder':'Return MM-DD-YYYY'}), label='')
    
    class Meta:
        model = Flight
        fields = '__all__'
        widgets={
            'flight_arrival': DateInput(),
            'flight_return': DateInput()
        }
    

class FlightChecker(forms.Form):
    
    flight_number = forms.CharField(max_length=6, label=False)
    
