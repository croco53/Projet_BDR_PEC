#-*- coding: utf-8 -*-

#from appli.models import Locations, Event, Airport, Aircraft

import pandas as pd
import datetime

data=pd.read_csv("aeropuerto.csv", sep=";")

data1=pd.read_csv("compagnos.csv", sep=";",encoding='latin-1')

data2=pd.read_csv("camino.csv", sep=";")


#Table aeroports

for i in range (500) :
    a = aero(id_aero=data[i,"id_aero"], nom_aero=data[i,"nom_aero"], ville_aero=data[i,"ville_aero"] , pays_aero=data[i,"pays_aero"], gmt_aero=data[i,"gmt_aero"])
    a.save()

print("this is goood")
  
  

#Table compagnies 

for i in range (len(data1)) :
    b = comp(id_comp=data1[i,"id_comp"], nom_comp=data1[i,"nom_comp"], 
              pays_comp=data1[i,"pays_comp"
    b.save()
print("this is goood too")
    


# Table routes
    
for i in range (len(data2)):
    c = route(id_route=data2[i,"id_route"], id_comp=data2[i,"id_comp"], id_aero_dep=data2[i,"id_aero_dep"],id_aero_arr=data2[i,"id_aero_arr"])
    c.save()
print("amazing")
    





