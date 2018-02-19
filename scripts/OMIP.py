# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 13:56:13 2017

@author: poliver
"""

# importem llibreries
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import matplotlib.pyplot as plt
import datetime as DT
import calendar

#Obrir arxiu
OMIP_brut_df = pd.read_csv('MIBEL_Contracts_23-10-2017_529.csv',sep=';',header=1,engine='python',decimal=',', parse_dates=['Day'])

#Agafa les columnes que volem i borrar files <> FTB
OMIP_brut_df = OMIP_brut_df[['Day','Contract','Settlement Price']]
OMIP_FTB_df = OMIP_brut_df[OMIP_brut_df["Contract"].str.contains('FTB')==True]

#Canvio format de data per poder-la graficar amb plt
data = OMIP_FTB_df['Day'].astype(DT.datetime)

#Crea una columna amb el número del mes de Day
#OMIP_FTB_df['monthNumer'] = pd.DatetimeIndex(OMIP_FTB_df['Day']).month

#definim 2 indexs
OMIP_FTB_df.set_index(["Contract"], ['monthNumber'])
preu_mig = OMIP_FTB_df.groupby(['Contract'])['Settlement Price'].mean()

#Definicions de periodes
now= DT.datetime.now()
ANY=now.year-2000
MES=now.month
MONTH= [ MES+1, MES+2, MES+3, MES+4]
YR= [ ANY+1, ANY+2, ANY+3, ANY+4]

#FTB_YR=pd.DataFrame()
#for item in YR:
#    any_filtrat = [OMIP_FTB_df["Contract"].str.contains('FTB YR-' + str(item))==True]
#    FTB_YR.append(any_filtrat)

#FTB_YR2_df = OMIP_FTB_df[OMIP_FTB_df["Contract"].str.contains('FTB YR-' + str(ANY+2)[2:])==True]
#FTB_YR3_df = OMIP_FTB_df[OMIP_FTB_df["Contract"].str.contains('FTB YR-'+ str(ANY+3)[2:])==True]
#FTB_YR4_df = OMIP_FTB_df[OMIP_FTB_df["Contract"].str.contains('FTB YR-'+ str(ANY+4)[2:])==True]

#Crear df per cada M
FTB_M1_df = OMIP_FTB_df[OMIP_FTB_df["Contract"].str.contains('FTB M Nov-17')==True]
FTB_M2_df = OMIP_FTB_df[OMIP_FTB_df["Contract"].str.contains('FTB M Dec-17')==True]
FTB_M3_df = OMIP_FTB_df[OMIP_FTB_df["Contract"].str.contains('FTB M Jan-18')==True]
FTB_M4_df = OMIP_FTB_df[OMIP_FTB_df["Contract"].str.contains('FTB M Feb-18')==True]


##PLot Y
#y= FTB_YR1_df['Day']
#y1= FTB_YR1_df['Settlement Price']
#y2= FTB_YR2_df['Settlement Price']
#y3= FTB_YR3_df['Settlement Price']
#y4= FTB_YR4_df['Settlement Price']
#
#figY = plt.figure(0)
#plt.plot_date(y, y1,'.')
#plt.plot_date(y, y2,'.')
#plt.plot_date(y, y3,'.')
#plt.plot_date(y, y4,'.')
#
##Configuració gràfic YR
#plt.title("Evolució OMIP (YR)")
#plt.legend(YR)
#plt.xlabel('Data')
#plt.ylabel('Preu (€/MWh)')
#plt.savefig('YR_OMIP.png')

#PLot M
a= FTB_M1_df['Day']
b= FTB_M2_df['Day']
c= FTB_M3_df['Day']
d= FTB_M4_df['Day']
m1= FTB_M1_df['Settlement Price']
m2= FTB_M2_df['Settlement Price']
m3= FTB_M3_df['Settlement Price']
m4= FTB_M4_df['Settlement Price']

figM = plt.figure(1)
plt.plot_date(a, m1, '+')
plt.plot_date(b, m2,'+')
plt.plot_date(c, m3,'+')
plt.plot_date(d, m4,'+')

#Configuració gràfic M
plt.title("Evolució OMIP (M)")
plt.legend(MONTH)
plt.xlabel('Data')
plt.ylabel('Preu (€/MWh)')
plt.savefig('M_OMIP.png')

#Taula dinamica prova


