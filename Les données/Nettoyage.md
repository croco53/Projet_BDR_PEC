# Nettoyage de nos données

Tout d'abord, au vu de notre sujet nous a décidé d'utiliser seulement ce [lien](https://openflights.org/data.html). Puis nous avons téléchargé les 3 bases de données suivantes ***aéroports.dat***, ***airlines.dat***, ainsi que ***routes.dat*** (la description de celles-ci a été faite dans le document _Extraction.md_ dans le dossier _Les données brutes_. 

---

A l'aide de _Excel_, nous avons dans un premier mis ces 3 bases de données sous format __CSV__, nous avons donc respectivement ***aero.csv***, ***comp.csv*** et ***route.csv***. Puis, nous avons supprimé les colonnes qui ne nous semblaient pas utiles pour notre projet :

* aero.csv : Nous avons supprimé __IATA__, __ICAO__, __Latitude__, __Longitude__, __Altitude__, __DST__, __Tz database time zone__, __Type__ et __Source__. 

* comp.csv : __Alias__, __IATA__, __ICAO__, __Callsign__ et __Active__.
* route.csv : __Airline__, __Source airport_, __Destination airport__, __Codeshare__, __Stops__, __Equipment.

