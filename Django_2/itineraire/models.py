from django.db import models

# Create your models here.
from django.db import models

class aero(models.Model):
    IACO = models.CharField(primary_key=True, max_length=4,unique=True)
    airport_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lat = models.CharField(max_length = 30)
    lon = models.CharField(max_length = 30)

class comp(models.Model):
    IACO = models.CharField(primary_key=True, max_length=4,unique=True)
    airport_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    lat = models.CharField(max_length = 30)
    lon = models.CharField(max_length = 30)

class route(models.Model):
    date = models.CharField(max_length = 4)
    location = models.CharField(max_length = 100)
    incident_country = models.CharField(max_length = 100)
    plane_type = models.CharField(max_length = 100)
    airport_dep = models.ForeignKey(Airports_dep, on_delete=models.CASCADE)#revoir si cascade justifiée
    airport_arr = models.ForeignKey(Airports_arr, on_delete=models.CASCADE)#idem

