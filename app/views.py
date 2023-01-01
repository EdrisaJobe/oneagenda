from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserEmail, FlightForm, HotelForm
from .models import Flight, Hotel

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

# handle the flight deletion
def delete_flight(request):
    
    if request.method == "POST":
        id = request.POST.get("id")
        fl = Flight.objects.get(id=id)
        fl.delete()
        return redirect('flight_agenda')

# hanfle the hotel deletion
def delete_hotel(request):

    if request.method == "POST":
        id = request.POST.get("id")
        ht = Hotel.objects.get(id=id)
        ht.delete()
        return redirect('hotel_agenda')


@login_required
def flight_agenda(request):
    
    # grab all the saved items within database upon user request
    flight_list = Flight.objects.filter(user=request.user)

    if request.method == "POST":
        form = FlightForm(request.POST)

        if form.is_valid():
            
            # get each individual item
            flight_number = form.cleaned_data['flight_number']
            flight_origin = form.cleaned_data['flight_origin']
            flight_destination = form.cleaned_data['flight_destination']
            flight_gate = form.cleaned_data['flight_gate']
            flight_seat = form.cleaned_data['flight_seat']
            flight_arrival = form.cleaned_data['flight_arrival']
            flight_return = form.cleaned_data['flight_return']

            # if user input, we save to individual db
            form.instance.user = request.user
            form.save()
            return redirect('flight_agenda')
        
    else:
        form = FlightForm()

    return render(request, 'app/pages/flight_agenda.html', {'form': form, 'flight_list': flight_list})

@login_required
def hotel_agenda(request):

    # save data to individual
    hotel_list = Hotel.objects.filter(user=request.user)

    if request.method == "POST":
        form = HotelForm(request.POST)

        if form.is_valid():

            hotel_origin = form.cleaned_data['hotel_origin']
            hotel_destination = form.cleaned_data['hotel_destination']
            hotel_arrival = form.cleaned_data['hotel_arrival']
            hotel_return = form.cleaned_data['hotel_return']
            hotel_travelers = form.cleaned_data['hotel_travelers']

            form.instance.user = request.user
            form.save()
            return redirect('hotel_agenda')
    else:
        form = HotelForm()

    return render(request, 'app/pages/hotel_agenda.html', {'form':form, 'hotel_list':hotel_list})
