"""securewaypoint URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app import views

urlpatterns = [

    # Registration/models
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')), # login page
    path('register/', views.register, name='register'),

    # When user deletes a flight or hotel model
    path('delete_flight/', views.delete_flight, name='delete_flight'),
    path('dleete_hotel/', views.delete_hotel, name='delete_hotel'),
    
    # Pages
    path('', views.home, name='home'),
    path('flight-agenda/', views.flight_agenda, name='flight_agenda'),
    path('hotel-agenda/', views.hotel_agenda, name='hotel_agenda')
   
]
