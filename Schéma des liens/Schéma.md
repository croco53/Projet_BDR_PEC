# Explication du  système d'association

Tout d'abord, pour créer notre  *modèle entité-association* , on a utilisé _SQL_ _Power_ _architect_ .

---

Notre modèle est constitué de _3_ _entités_ constituées chacunes de plusieurs attributs :

* _aeroport_ :
  * id_aero
  * ville_aero
  * gmt_aero
  * pays_aero

* _compagnie_ :
  * id_comp
  * nom_comp
  * pays_comp 
  
* _route_ :
  * id_route
  * id_comp
  * id_aero_dep
  * id_aero_arr


