"""Django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    #   path('', views.home),
    path('', views.accueil),
    path('about/', views.about),
    path('contact/', views.contact),
    path('route/', views.route),
    path('compagnie/', views.compagnie),
    path('aeroport/', views.aeroport),
    path('comp/', views.affichage_comp),
    path('iti/', views.affichage_route),
    path('aero/', views.affichage_aero),
    path('recherche/', views.recherche),
    path('search/search_aero/', views.search_aero),
    path('search/search_comp/', views.search_comp),
    path('search/search_pays/', views.recherche),
    path('search/search_route/', views.search_route),
    path('search/', views.search),
    path('blog/', views.blog),

    path('admin/', admin.site.urls),
]
