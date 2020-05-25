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
