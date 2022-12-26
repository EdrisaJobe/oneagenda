from django.shortcuts import render, redirect
from .forms import UserEmail
from django.contrib import messages

### USER AUTHENTICATION ###
def register(response):

    if response.method == "POST":
        form = UserEmail(response.POST)
        if form.is_valid():
            form.save()
            messages.success(response, "Registration Successful!")
        return redirect('/login')
    else:
        form = UserEmail()
    return render(response, 'registration/register.html', {'form':form})
### ENDOF USER AUTHENTICATION ###

### PAGES ###
def home(request):
    
    return render(request, 'app/pages/home.html')

def book(request):

    return render(request, 'app/pages/book.html')
### ENDOF PAGES ###