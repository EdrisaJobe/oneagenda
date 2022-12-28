from django.db import models

# Create your models here.
class Flight(models.Model):
    
    flight_number = models.CharField(max_length=6)
    flight_origin = models.CharField(max_length=3)
    flight_destination = models.CharField(max_length=3)
    flight_arrival = models.DateField(auto_now=False)
    flight_return = models.DateField(auto_now=False)