# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 11:55:49 2017

@author: poliver
"""

import pandas as pd
from pandas import Series,DataFrame
from pandas import ExcelWriter


# obrir excel
mesures_df   = pd.ExcelFile("mesures.xlsx")
mesures_df = mesures_df.parse('hoja1')
print("Inicial", len(mesures_df))

#Recompte hores, borrar si no tenen les 24
mesures_df=mesures_df.dropna(subset = ['H1', 'H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15','H16','H17','H18', 'H19', 'H20','H21','H22','H23','H24'])

#borrar duplicats
mesures_df = mesures_df.drop_duplicates(subset=['cups', 'fecha'], keep='first')

#Tarifes 6.1B i 6.2 a 6.1
mesures_df['TarifaAcceso'] = mesures_df['TarifaAcceso'].replace(['6.1B', '6.2'], '6.1')

#Creem seie_df i peninsula_df
seie_df = mesures_df[mesures_df["Subsistema"].str.contains('P')==False]
peninsula_df = mesures_df[mesures_df["Subsistema"].str.contains('P')==True]

#info dels df
print("Península",len(peninsula_df))
print("Seie",len(seie_df))

#Generarem dos excels amb les mesures tractades
writer = ExcelWriter('mesures_netes.xlsx')
peninsula_df.to_excel(writer,'peninsula')
seie_df.to_excel(writer,'seie')
writer.save()
print("Procés finalitzat")
