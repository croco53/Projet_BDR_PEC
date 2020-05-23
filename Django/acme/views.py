#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 23 02:26:49 2020

@author: pierrine
"""
from django.http import HttpResponse
from django.shortcuts import render

#def home(request):
    
#    return render(request, 'home.html')

#HttpResponse('Vous avez la tête dans les nuages? On se charge de trouver votre itinéraire')

#def about(request):
 #  return render(request, 'page/about.html')

#def contact(request):
 #  return render(request, 'page/contact.html')

def accueil(request):

   return render (request, 'accueil.html')