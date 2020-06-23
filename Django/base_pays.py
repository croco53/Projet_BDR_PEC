#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:40:57 2020

@author: pierrine
"""

Created on Mon Mar 30 17:36:00 2020



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


def data_country():
    tab = []
    with open("/users/pierrine/Desktop/data_country.csv", 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for line in reader:
            tab.append((line[0].split(',')[0], line[1].split(
                ',')[0], line[2].split(',')[0]))
    return tab

###############################################################################


data = data_country()
cur = conn.cursor()
for i in range(1, len(data)):
    cur.execute("""
        INSERT INTO  public."appli_pays"(id_pays,nom_pays)
        VALUES (%s,%s);
        """,
                (data[i][2], data[i][1]))
sys.stdout.write('Insertion réussie...')

###############################################################################

cur.close()
conn.commit()
conn.close()
sys.stdout.write('Opération terminée avec Succès')

###############################################################################
