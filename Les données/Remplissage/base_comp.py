#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 15:40:16 2020

@author: pierrine
"""


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


def data_comp():
    tab = []
    with open('/users/pierrine/Desktop/compagnie_propre.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            tab.append((line[0].split(',')[0], line[1].split(',')[0],
                        line[2].split(',')[0]))
    return tab

###############################################################################


data = data_comp()
cur = conn.cursor()
for i in range(1, len(data)-1):
    cur.execute("""
        INSERT INTO  postgres."postgres"(id_comp,nom_comp,pays_comp)
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