# Explication du  système d'association

Tout d'abord, pour créer notre  *modèle entité-association* , on a utilisé __SQL Power architect__ .

---

Notre modèle est constitué de _3 entités_ constituées chacunes de plusieurs _attributs_ :

* __aeroport__ :
  * id_aero (clé primaire de la table __aeroport__ , elle définit de manière unique chaque enregistrement 
  de la table __aeroport__ )
  * ville_aero
  * gmt_aero
  * pays_aero

* __compagnie__ :
  * id_comp (clé primaire de la table __compagnie__ )
  * nom_comp
  * pays_comp 
  
* __route__ :
  * id_route (clé primaire de la table __route__ )
  * id_comp
  * id_aero_dep
  * id_aero_arr

---

Les _associations_ entre nos différentes tables :

* association entre __compagnie__ et __route__ : Une compagnie aérienne a plusieurs itinéraires possibles et un itinéraires peut être proposé par plusieurs compagnies. 

* association entre __aeroport__ et __route__ : Même chose que pour compagnie, un aéroport propose plusieurs itinéraires et un itinéraire peut également être proposé par différents aéroport.


