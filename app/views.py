from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserEmail, FlightForm
import requests

### USER AUTHENTICATION ###


def register(request):

    if request.method == "POST":
        form = UserEmail(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, "Successfully Registered!")
            return redirect('/login')
    else:
        form = UserEmail()

    return render(request, 'registration/register.html', {'form': form})
### ENDOF USER AUTHENTICATION ###


def home(request):

    return render(request, 'app/pages/home.html')

def flight_agenda(request):
    
    form = FlightForm()
    
    if request.method == "POST":
        form = FlightForm(request.POST)
        if form.is_valid():
            
            form.save()
            return redirect('flight_agenda')

    return render(request, 'app/pages/flight_agenda.html', {'form':form})


def book_hotel(request):

    return render(request, 'app/pages/book_hotel.html')
