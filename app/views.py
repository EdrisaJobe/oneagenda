from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserEmail

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
    
    return render(request, 'registration/register.html', {'form':form})
### ENDOF USER AUTHENTICATION ###

### PAGES ###
def home(request):
    
    return render(request, 'app/pages/home.html')

def book(request):

    return render(request, 'app/pages/book.html')
### ENDOF PAGES ###