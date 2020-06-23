#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:19:39 2020
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


def data_airline():
    tab = []
    with open('/users/pierrine/Desktop/data_airline.csv', 'r', encoding='latin-1') as f:
        reader = csv.reader(f)
        for line in reader:
            tab.append((line[0].split(',')[0], line[1].split(',')[0],
                        line[2].split(',')[0], line[3].split(',')[0], line[4].split(',')[0]))
    return tab

###############################################################################


data = data_airline()
cur = conn.cursor()
for i in range(1, len(data)):
    cur.execute("""
        INSERT INTO  public."appli_comp"(id_comp,nom_comp,actif,id_pays_id)
        VALUES (%s,%s,%s,%s);
        """,
                (data[i][4], data[i][1], data[i][2], data[i][3]))
sys.stdout.write('Insertion réussie...')

###############################################################################

cur.close()
conn.commit()
conn.close()
sys.stdout.write('Opération terminée avec Succès...')

###############################################################################
