from django.shortcuts import render
from . import views

# Create your views here.
from django.http import HttpResponse
from .models import aeroports,compagnie,route
import datetime
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_agg import FigureCanvasAgg

# Create your views here.

def index(request):

    pass


def compagnie(request):
    if not request.GET.keys():
        return render(request, 'compagnie.tmpl',
                      {
                          'compagnie': Compagnie.objects.all().order_by('nom_compagnie'),
                          'nb': Compagnie.objects.count() - 1,
                          'rien': Compagnie.objects.count() == 0
                      })

    else:
        comp = Compagnie.objects.all()
        rech_compagnie = request.GET['rech_compagnie']
        if 'rech_compagnie' in request.GET.keys():
            comp = comp & Compagnie.objects.filter(nom_compagnie__icontains=rech_compagnie)
        if 'chercher_alias' in request.GET.keys():
            alias = Compagnie.objects.filter(alias__icontains=rech_compagnie)
            comp = comp & alias

        chercher_pays = request.GET['chercher_pays']
        if not chercher_pays == '':
            pays = Pays.objects.filter(nom_pays__icontains=chercher_pays)
            pa = Compagnie.objects.filter(nom_pays__in=pays)
            comp = comp & pa
        return render(request, 'compagnie.tmpl',
                      {
                          'compagnie': comp.order_by('nom_compagnie'),
                          'nb': comp.count(),
                          'rien': comp.count() == 0
                      })


def aeroport(request):
    if not request.GET.keys():
        return render(request, 'aeroport.html',
                      {
                          'aeroport': Aeroport.objects.all().order_by('nom_aeroport'),
                          'nb': Aeroport.objects.count() - 1,
                          'rien': Aeroport.objects.count() == 0
                      })

    else:
        liste = Aeroport.objects.all()
        aero = request.GET['aero']
        if not aero == '':
            nom = Aeroport.objects.filter(nom_aeroport__icontains=aero)
            liste = liste & nom

        if 'chercher_ville' in request.GET.keys():
            ville = Ville.objects.filter(nom_ville__icontains=vipa)
            ae = Aeroport.objects.filter(ville__in=ville)
            liste = liste & ae

        if 'chercher_pays' in request.GET.keys():
            pays = Pays.objects.filter(nom_pays__icontains=vipa)
            ville = Ville.objects.filter(nom_pays__in=pays)
            ae = Aeroport.objects.filter(ville__in=ville)
            liste = liste & ae

        return render(request, 'aeroport.html',
                      {
                          'aeroport': vi_pa.order_by('nom_aeroport'),
                          'nb': vi_pa.count(),
                          'rien': vi_pa.count() == 0
                      })
