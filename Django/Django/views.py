#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 02:26:49 2020
@author: pierrine
"""
from django.http import HttpResponse
from django.shortcuts import render

from appli.models import *
from .filtre import *

# def home(request):

#    return render(request, 'home.html')

# HttpResponse('Vous avez la tête dans les nuages? On se charge de trouver votre itinéraire')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def blog(request):
    return render(request, 'blog.html')

def accueil(request):
    return render(request, 'index2.html')

def search_pays(request):
    return render(request, 'search_pays_sure.html')

def search_aero(request):
    aero = Aero.objects.all()
    aero_filter = Filtre_aero(request.GET, queryset = aero)
    aero = aero_filter.qs
    return render(request, 'search_aero.html',{'aero': aero, 'aero_filter': aero_filter})

def search_comp(request):
    comp = Comp.objects.all()
    comp_filter = Filtre_comp(request.GET, queryset = comp)
    comp = comp_filter.qs
    return render(request, 'search_comp.html',{'comp': comp, 'comp_filter': comp_filter})

def search_route(request):
    route = Route.objects.all()
    route_filter = Filtre_route(request.GET, queryset = route)
    route = route_filter.qs
    return render(request, 'search_route.html',{'route': route, 'route_filter': route_filter})

def search(request):
    return render(request, 'search.html')

def recherche(request):
    pays=Pays.objects.all()
    pays_filter = Filtre_pays(request.GET, queryset=pays)
    pays= pays_filter.qs
    return render(request, 'search_pays.html', {'pays': pays, 'pays_filter': pays_filter})


def route(request):
    return render(request, 'route.html')


def compagnie(request):
    return render(request, 'compagnie.html')

def aeroport(request):
    return render(request, 'aeroport.html')

def affichage_comp(request):
    comps= [
        {'id_c': 1, 'id_comp': '24', 'nom_comp': 'American Airlines' , 'pays_comp': 'United States'},
        {'id_c': 2, 'id_comp' : '137', 'nom_comp' : 'Air France', 'pays_comp' : 'France'},
        {'id_c': 3, 'id_comp' : '596', 'nom_comp' : 'Alitalia', 'pays_comp' : 'Italy'}

    ]
    return render (request, 'affichage_comp.html', {'comps' : comps })

def affichage_aero(request):
    aeros= [
        {'id_a' : 1, 'id_aero': '1382', 'nom_aero': 'Charles de Gaulles International Airport' , 'ville_aero': 'Paris', 'gmt_aero': '1', 'pays_aero': 'France'},
        {'id_a': 2, 'id_aero' : '507', 'nom_aero' : 'London Heathrow Airport', 'ville_aero' : 'London', 'gmt_aero' : '0', 'pays_aero' : 'United Kingdom'},
        {'id_a': 3,'id_aero' : '3797', 'nom_aero' : 'John F Kennedy International Airport', 'ville_aero' : 'New York', 'gmt_aero' : '-5', 'pays_aero' : 'United States'}

    ]
    return render (request, 'affichage_aero.html', {'aeros' : aeros })

def affichage_route(request):
    itis = [
        {'id_r': 1, 'id_route' : '2127', 'id_comp_route' : '24', 'id_aero_dep': '1382', 'id_aero_arr': '507'},
        {'id_r': 2, 'id_route' : '5014', 'id_comp_route' : '137', 'id_aero_dep' : '507', 'id_aero_arr' : '3797'},
        {'id_r': 3, 'id_route' : '11196', 'id_comp_route' : '596', 'id_aero_dep' : '3797', 'id_aero_arr' : '1392'}

    ]
    return render(request, 'affichage_route.html', {'itis': itis})