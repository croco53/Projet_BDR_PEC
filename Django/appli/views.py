from django.shortcuts import render

# Create your views here.

from .models import *

def recherche(request):
    pays=Pays.objects.all()
    return render(request, 'recherche_pays.html', {'pays': pays})