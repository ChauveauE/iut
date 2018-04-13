#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import erppeek
import datetime

#connexion à erppeek
server = 'http://localhost:8071'
database = 'Test1'
user = 'elodie.chauveau@etu.univ-nantes.fr'
password = 'admin'

client = erppeek.Client(server, db=database, user=user, password=password)

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


#on recherche si les éléments du fichier csv existent déjà en bdd
# Si "0": les valeurs du doc csv sont différentes de celle de la BDD
# Si "1": les valeurs du doc csv sont identiques à celle de la BDD => message de non insertion

#recherche de la marque
envBrand = client.search('iut.it.brand', [('name', '=', row[4])])
print ('Il existe {} marque identique'.format(len(envBrand)))

#recherche du type de modèle
envModelType = client.search('iut.it.model.type', [('name', '=', row[5])])
print ('Il existe {} modèle type identique'.format(len(envModelType)))

#recherche du modèle
envModel = client.search('iut.it.model', [('name', '=', row[3])])
print ('Il existe {} modèle identique'.format(len(envModel)))

#recherche de l'employé
envPartner = client.search('res.partner', [('name', '=', row[6])])
print ('Il existe {} employé identique'.format(len(envPartner)))

#recherche du dispositif
envDevice = client.search('iut.it.device', [('serial_number','=', row[0]), ('date_allocation','=', row[1]), ('date_purchase','=', row[2])])
print ('Il existe {} dispositif identique'.format(len(envDevice)))

print('')

#insertion des données dans la bdd si elles n'existent pas

#ajout des valeurs de la marque
if len(envBrand) == 0:
     vBrand = client.create('iut.it.brand', {'name':row[4], 'warranty_delay_month':12})
else:
    vBrand = envBrand[0]
    print('insertion non possible')

#ajout des valeurs du type de modèle
if len(envModelType) == 0:
     vModelType = client.create('iut.it.model.type', {'name': row[5]})
else:
    vModelType = envModelType[0]
    print('insertion non possible')

#ajout des valeurs du modèle
if len(envModel) == 0:
     vModel = client.create('iut.it.model', {'name': row[3], 'brand_id': vBrand})
else:
    vModel = envModel[0]
    print('insertion non possible')

#ajout des valeurs de l'employé
if len(envPartner) == 0:
     vPartner = client.create('res.partner', {'name': row[6]})
else:
    vPartner = envPartner[0]
    print('insertion non possible')

#ajout des valeurs du dispositif
if len(envDevice) == 0:
     vDevice = client.create('iut.it.device', {'name': 'xxx', 
                                                'serial_number': row[0], 
                                                'date_allocation': row[1], 
                                                'date_purchase': row[2], 
                                                'partner_id': vPartner, 
                                                'model_id': vModel})
else:
    vDevice = envDevice[0]
    print('insertion non possible')