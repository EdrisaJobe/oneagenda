from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserEmail, FlightForm
from .models import Flight

### USER AUTHENTICATION ###
def register(request):

    if request.method == "POST":
        form = UserEmail(request.POST)
        if form.is_valid():
            form.save()

            # success message at login
            messages.success(request, "Successfully Registered!")
            return redirect('/login')
    else:
        form = UserEmail()

    return render(request, 'registration/register.html', {'form': form})
### ENDOF USER AUTHENTICATION ###

def home(request):

    return render(request, 'app/pages/home.html')

@login_required
def flight_agenda(request):
    
    # grab all the saved items within database
    flight_list = Flight.objects.filter(user=request.user)

    if request.method == "POST":
        form = FlightForm(request.POST)

        if form.is_valid():
            
            # get each individual item
            flight_number = form.cleaned_data['flight_number']
            flight_origin = form.cleaned_data['flight_origin']
            flight_destination = form.cleaned_data['flight_destination']
            flight_arrival = form.cleaned_data['flight_arrival']
            flight_return = form.cleaned_data['flight_return']

            form.instance.user = request.user
            form.save()
            return redirect('flight_agenda')

    else:
        form = FlightForm()

    return render(request, 'app/pages/flight_agenda.html', {'form': form, 'flight_list': flight_list})


def book_hotel(request):

    return render(request, 'app/pages/book_hotel.html')
