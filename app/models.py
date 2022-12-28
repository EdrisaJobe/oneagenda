from django.db import models

# Create your models here.
class Flight(models.Model):
    
    flight_number = models.CharField(max_length=6)
    origin = models.CharField(max_length=3)
    destination = models.CharField(max_length=3)
    status = models.CharField(max_length=20)