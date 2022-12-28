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
        
class FlightForm(ModelForm):
    
    flight_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Flight number...'}), label='')
    origin = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'From'}), label='')
    destination = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'To'}), label='')
    status = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Status'}), label='')
    
    class Meta:
        model = Flight
        fields = '__all__'
    

class FlightChecker(forms.Form):
    
    flight_number = forms.CharField(max_length=6, label=False)
    
