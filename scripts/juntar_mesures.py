# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 16:34:45 2017

@author: poliver
"""
import os
import pandas as pd
from pandas import Series,DataFrame
from pandas import ExcelWriter

path = os.getcwd() #dona la ruta de l'script
files = os.listdir(path) #llista els arxius de la carpeta
files

files_prev = [f for f in files if f[0:15] == 'CONSUMOS DIARIO'] #filtra els arxius que comencen amb aquest txt
files_prev
previsions_df = pd.DataFrame()
for f in files_prev:
    data = pd.read_excel(f, 'Listado_Previsiones_BC_RINGC01_') #especifica la pg de l'excel que s'ha de llegir
    previsions_df = previsions_df.append(data)
    previsions_df
    print(f, len(data))
 #Canviar 6.2 i 6.1B per 6.1
previsions_df['tarifaAcceso'] = previsions_df['tarifaAcceso'].replace(['6.1B', '6.2'], '6.1')
print('TOTAL:', len(previsions_df))
 
#Generarem excel amb un sol llistat de previsions
writer = ExcelWriter('previsions_juntes.xlsx')
previsions_df.to_excel(writer,'previsions')
writer.save()
print("Procés finalitzat")
