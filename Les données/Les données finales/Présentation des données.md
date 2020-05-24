# Présentation de nos données finales :

Nous avons donc 3 bases de données :

## __aero.csv__ composée de :
* id_aero : Identifiant unique de l'aéroport
* nom_aero : Nom de l'aéroport
* ville_aero : Ville de l'aéroport 
* pays_aero : Pays de l'aéroport
* gmt_aero : Fuseau horaire (heures décalées par rapport à UTC)
    
 ## __comp.csv__ composée de :
* id_comp : Identifiant unique de la compagnie aérienne
* nom_comp : Nom de la compagnie aérienne
* pays_comp : Pays de la compagnie aérienne 
    
 ## __route.csv__ composée de :
* id_route : Identifiant unique de l'itinéraire
* id_comp_route : Identifiant unique de la compagnie aérienne
* id_aero_dep : Identifiant unique de l'aéroport de départ 
* id_aero_arr : Identifiant unique de l'aéroport d'arrivée
