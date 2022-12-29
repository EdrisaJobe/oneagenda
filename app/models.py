from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flight(models.Model):
    
    flight_number = models.CharField(max_length=6)
    flight_origin = models.CharField(max_length=3)
    flight_destination = models.CharField(max_length=3)
    flight_gate = models.CharField(max_length=3, null=True)
    flight_seat = models.CharField(max_length=3, null=True)
    flight_arrival = models.DateField(auto_now=True)
    flight_return = models.DateField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)