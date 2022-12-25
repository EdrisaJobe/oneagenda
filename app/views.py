from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'app/pages/home.html')

def book(request):

    return render(request, 'app/pages/book.html')