#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import os


#lecture du fichier csv
with open('device.csv', 'r') as csvFile:
    csvr = csv.reader(csvFile)                          #csvr : csv reader
    for row in csvr:
       # print(row)                                     # affichage de toutes les données
       print('numero de serie : {}'.format(row[0]))     # affichage du numero de serie
       print('date allocation : {}'.format(row[1]))     # affichage de la date d'allocation  
       print('date achat : {}'.format(row[2]))          # affichage de la date d'achat
       print('modele : {}'.format(row[3]))              # affichage du modele
       print('marque : {}'.format(row[4]))              # affichage de la marque
       print('type : {}'.format(row[5]))                # affichage du type
       print('employe : {}'.format(row[6]))             # affichage de l'employe
       print('')


# serial number
# date allocation
# date purchase
# model name
# marque
# modelType name
# partner nom
