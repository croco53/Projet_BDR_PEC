#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 22:16:58 2020

@author: pierrine
"""

###############################################################################

import psycopg2
import sys
import csv

###############################################################################






try:
    conn = psycopg2.connect( database='postgres',user="postgres", password='Postgredemerde')
    sys.stdout.write('Connexion établie...')
except psycopg2.Error:
    sys.stdout.write('connexion échouée...\n')
    sys.exit()

###############################################################################


def data_aero():
    tab = []
    with open('/users/pierrine/Desktop/aeroport_propre.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            tab.append((line[0].split(',')[0], line[1].split(',')[0],
                        line[2].split(',')[0], line[3].split(',')[0]))
    return tab

###############################################################################


data = data_aero()
cur = conn.cursor()
for i in range(1, len(data)-1):
    cur.execute("""
        INSERT INTO  postgres."postgres"(id_aero,nom_aero,ville_aero,gmt_aero)
        VALUES (%s,%s,%s,%s);
        """,
                ( data[i][1], data[i][2], data[i][3]))
sys.stdout.write('Insertion réussie...')

###############################################################################

cur.close()
conn.commit()
conn.close()
sys.stdout.write('Opération terminée avec Succès...')

###############################################################################