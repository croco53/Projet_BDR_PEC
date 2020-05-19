Extraction des données brutes
=
L'ensemble de l'extration des données a été effectué sur le [site](https://openflights.org/data.html)

Concrètement, nous avons extrait 3 bases de donnée qui sont composées  comme suit:

_airports.dat_ 
-
 * _ID_ _de_ _l'aéroport_ : Identifiant unique pour l'aéroport  
 * _Nom_ : Nom de l'aéroport
 * _Pays_ : Pays ou territoire où se trouve l'aéroport
 * _IATA_ : Code IATA à 3 lettres (Nul si non attribué / inconnu)
 * _OACI_ : Code OACI à 4 lettres (Nul si non attribué)
 * _Latitude_ : Degrés décimaux, généralement à six chiffres significatifs (négatif est Sud, positif est Nord)
 * _Longitude_ : Degrés décimaux, généralement à six chiffres significatifs (négatif est Ouest, positif est Est)
 * _Altitude_ : En pieds
 * _Fuseau_ _horaire_ : Heures décalées par rapport à UTC. Les heures fractionnaires sont exprimées en décimales
 * _DST_ : 	Le temps de l'heure d'été
 * _Fuseau_ _horaire_ _de_ _la_ _base_ _de_ _données_ _TZ_ : Fuseau horaire au format "tz" (Olson) 
 * _Type_ : Type d'aéroport. Valeur "aéroport" pour les aérogares, "gare" pour les gares, "port" pour les terminaux de ferry et "inconnu" s'il n'est pas connu
 * _La_ _source_ : Source de ces données. "OurAirports" pour les données provenant de OurAirports , "Legacy" pour les anciennes données qui ne correspondent pas à OurAirports (principalement DAFIF), "User" pour les contributions des utilisateurs non vérifiées. Dans aéroports.csv, seule la source = OurAirports est incluse
 
 _airlines.dat_
 -
 * _ID_ _de_ _la_ _compagnie_ _aérienne_ : Identifiant unique de la compagnie aérienne
 * _Nom_ : Nom de la compagnie
 * _Alias_ : 	Alias de la compagnie aérienne. Par exemple, All Nippon Airways est communément appelée «ANA»
 * _IATA_ : Code IATA à 2 lettres (si disponible)
 * _OACI_ : Code OACI à 3 lettres (si disponible)
 * _Signe_ _d'appel_ : Indicatif de la compagnie aérienne
 * _Pays_ : Pays ou territoire où se trouve l'aéroport
 * _Actif_ : 	"Y" si la compagnie aérienne est ou a été opérationnelle jusqu'à récemment, "N" si elle est disparue. Ce champ n'est pas fiable: en particulier, les grandes compagnies aériennes qui ont cessé de voler depuis longtemps, mais qui n'ont pas vu leur code IATA réaffecté (par exemple, Ansett / AN), s'affichent incorrectement comme "Y"
 
 _routes.dat_
 -
 * _Compagnie_ _aérienne_ : Code à deux lettres (IATA) ou à trois lettres (OACI) de la compagnie aérienne
 * _ID_ _de_ _la_ _compagnie_ _aérienne_ : Identifiant unique de la compagnie aérienne
 * _Aéroport_ _source_ : Code à 3 lettres (IATA) ou à 4 lettres (OACI) de l'aéroport source
 * _ID_ _de_ _l'aéroport_ _source_: Identifiant unique pour l'aéroport source
 * _Aéroport_ _de_ _destination_: Code à 3 lettres (IATA) ou à 4 lettres (OACI) de l'aéroport de destination
 * _ID_ _de_ _l'aéroport_ _de_ _destination_: Identifiant unique pour l'aéroport de destination
 * _Partage_ _de_ _code_ : "Y" si ce vol est en partage de code (c'est-à-dire non exploité par la compagnie aérienne , mais par un autre transporteur)
 * _Arrête_ : Nombre d'arrêts sur ce vol ("0" pour direct)
 * _Équipement_ : Codes à 3 lettres pour le (s) type (s) d'avion généralement utilisés pour ce vol, séparés par des espaces
 
 
Les données sont encodées en UTF-8. La valeur spéciale \ N est utilisée pour "NULL" pour indiquer qu'aucune valeur n'est disponible et est automatiquement comprise par MySQL si elle est importée.
  
 
