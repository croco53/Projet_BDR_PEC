import django_filters
from django_filters import CharFilter

from appli.models import *


class Filtre_pays(django_filters.FilterSet):
    pays = CharFilter(field_name='nom_pays',
                       lookup_expr='icontains', label="Nom du pays")

    class Meta:
        model = Pays
        fields = []


class Filtre_comp(django_filters.FilterSet):
    comp = CharFilter(field_name='nom_comp',
                       lookup_expr='icontains', label="Nom de la compagnie")

    class Meta:
        model = Comp
        fields = []


class Filtre_route(django_filters.FilterSet):
    route = CharFilter(field_name='id_route',
                       lookup_expr='icontains', label="N° de l'itinéraire")

    class Meta:
        model = Route
        fields = []

class Filtre_aero(django_filters.FilterSet):
    aero = CharFilter(field_name='nom_aero',
                       lookup_expr='icontains', label="Nom de l'aéroport")

    class Meta:
        model = Aero
        fields = []

