# Nettoyage de nos données

Tout d'abord, au vu de notre sujet nous a décidé d'utiliser seulement ce [lien](https://openflights.org/data.html). Puis nous avons téléchargé les 3 bases de données suivantes ***aéroports.dat***, ***airlines.dat***, ainsi que ***routes.dat*** (la description de celles-ci a été faite dans le document _Extraction.md_ dans le dossier _Les données brutes_. 

---

A l'aide de _Excel_, nous avons dans un premier mis ces 3 bases de données sous format __CSV__, nous avons donc respectivement ***aero.csv***, ***comp.csv*** et ***route.csv***. Puis, nous avons supprimé les colonnes qui ne nous semblaient pas utiles pour notre projet :

* aero.csv : Nous avons supprimé __IATA__, __ICAO__, __Latitude__, __Longitude__, __Altitude__, __DST__, __Type__ et __Source__. 

* comp.csv : __Alias__, __IATA__, __ICAO__, __Callsign__ et __Active__.
* route.csv : __Airline__, __Source airport__, __Destination airport__, __Codeshare__, __Stops__ (On a voulu garder cette colonne car elle indique si c'est un vol direct, lorsque que cette variable est égale à 0, cependant on a remarqué qu'elle valait toujou, __Equipment__.

*Pour la variable __Stops__ (dans la base de données __route.csv__), dans un premier temps nous voulions la conserver car elle indique si un vol est direct, lorsque cette variable est égale à 0. Cependant, nous avons remarqué que celle-ci valait quasiment toujours 0, sauf dans quelques cas où elle valait 1. Par conséquent, nous avons jugé que celle-ci était inutile pour notre projet.*

---

Nous avons également supprimé les lignes lorsqu'une des variables était nulle et rajouté une colonne __id_route__ à la base de données __route.csv__. 


