from django.db import models


# Create your models here.

class Aero(models.Model):
    id_aero = models.CharField(primary_key=True, max_length=10, unique=True)
    nom_aero = models.CharField(max_length=100)
    ville_aero = models.CharField(max_length=100)
    pays_aero = models.CharField(max_length=100)
    gmt_aero = models.CharField(max_length=30)
    def __str__(self):
       return '%s %s %s %s %s' % (self.id_aero, self.nom_aero, self.ville_aero, self.pays_aero, self.gmt_aero)

class Pays(models.Model):
    id_pays = models.IntegerField(primary_key=True, unique=True)
    nom_pays = models.CharField(max_length=100)
    def __str__(self):
        return '%s %s' % (self.id_pays, self.nom_pays)

class Comp(models.Model):
    id_comp = models.CharField(primary_key=True, max_length=4, unique=True)
    nom_comp = models.CharField(max_length=100)
    actif = models.BooleanField(default=None)
    id_pays=models.ForeignKey(Pays, on_delete=models.CASCADE)
    def __str__(self):
        return '%s %s %s %s' % (self.id_comp, self.nom_comp, self.actif, self.id_pays)

class Route(models.Model):
    id_route = models.CharField(primary_key=True, max_length=1000, unique=True)
    id_comp = models.CharField(max_length=100)
    id_aero_dep = models.CharField(max_length=100)
    id_aero_arr = models.CharField(max_length=100)
    def __str__(self):
       return '%s %s %s %s' % (self.id_route, self.id_comp,self.id_aero_dep, self.id_aero_arr)




