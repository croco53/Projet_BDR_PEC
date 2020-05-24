from django.db import models

# Create your models here.
from django.db import models
class aero(models.Model):
    id_aero = models.CharField(primary_key=True, max_length=10,unique=True)
    nom_aero = models.CharField(max_length=100)
    ville_aero = models.CharField(max_length=100)
    pays_aero = models.CharField(max_length=100)
    gmt_aero = models.CharField(max_length = 30)


class comp(models.Model):
    id_comp = models.CharField(primary_key=True, max_length=4,unique=True)
    nom_comp = models.CharField(max_length=100)
    pays_comp = models.CharField(max_length=100)


class route(models.Model):
    id_route = models.CharField(max_length = 20000)
    id_comp= models.CharField(max_length = 100)
    id_aero_dep = models.CharField(max_length = 100)
    id_aero_arr = models.CharField(max_length = 100)




