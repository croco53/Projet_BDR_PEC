# Explication du  système d'association

Tout d'abord, pour créer notre  *modèle entité-association* , on a utilisé __SQL Power architect__ .

---

__Notre modèle est constitué de _3 entités_ constituées chacunes de plusieurs attributs :__

* __aeroport__ :
  * id_aero (clé primaire de la table __aeroport__ , elle définit de manière unique chaque enregistrement de la table __aeroport__ )
  * ville_aero
  * gmt_aero
  * pays_aero

* _compagnie_ :
  * id_comp (clé primaire de la table _compagnie_ )
  * nom_comp
  * pays_comp 
  
* _route_ :
  * id_route (clé primaire de la table _route_ )
  * id_comp
  * id_aero_dep
  * id_aero_arr

---

_Les_ _associations_ _entre_ _nos_ _différentes_ _tables_ :


