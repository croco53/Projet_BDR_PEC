#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 15:51:50 2020

@author: verron
"""

import pandas as pd
import numpy as np



col_aero=['id_aero','nom_aero','ville_aero','pays_aero','iata','icao','lat','lon','alt','gmt_aero','dst','Tz','Type','source']
aero=pd.read_csv('/Users/verron/Desktop/data_sale/airports.csv',sep=',',encoding='utf-8',names=col_aero)
aero.drop(['iata','icao','lat','lon','alt','dst','Tz','Type','source'],axis=1,inplace=True)
aero=aero.replace(r'\N',np.nan)
aero=aero.dropna(axis = 0, how = 'any')
aero=aero[['id_aero','nom_aero','ville_aero','gmt_aero']]


col_comp=['id_comp','nom_comp','alias','iata','iaco','callsign','pays_comp','active']
comp=pd.read_csv('/Users/verron/Desktop/data_sale/airlines.csv', sep=',',encoding='utf-8',names=col_comp)
comp.drop(['alias','iata','iaco','callsign','active'],axis=1,inplace=True)
comp=comp.replace(r'\N',np.nan)
comp=comp.dropna(axis = 0, how = 'any')




col_route=['code','id_comp','iaco_dep','id_aero_dep','iaco_arr','id_aero_arr','codeshare','stops','equipe']
route=pd.read_csv('/Users/verron/Desktop/data_sale/routes.csv', sep=',',encoding='utf-8',names=col_route)
route.drop(['code','iaco_dep','iaco_arr','codeshare','stops','equipe'],axis=1,inplace=True)
route=route.replace(r'\N',np.nan)
route=route.dropna(axis = 0, how = 'any')
route['id_route']=range(1,len(route)+1)
route=route[['id_route','id_aero_dep','id_aero_arr','id_comp']]


aero.to_csv (r'/Users/verron/Desktop/data_sale/aeroport_propre.csv', index = False)
comp.to_csv (r'/Users/verron/Desktop/data_sale/compagnie_propre.csv', index = False)
route.to_csv (r'/Users/verron/Desktop/data_sale/route_propre.csv', index = False)
