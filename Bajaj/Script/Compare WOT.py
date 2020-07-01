# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:51:59 2020

@author: nikhilp
"""
from asammdf import MDF
import easygui
import pandas as pd
import glob, os
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import binned_statistic_2d 



KS_filepath = easygui.fileopenbox(msg='Select excel files', default='*.xlsx', multiple = True)
folderPath = os.path.dirname(KS_filepath[0])

lis = []
for i in range(0,len(KS_filepath)):
    a = input("Enter Legend") #for",i,'st Modal')

    lis.append(a)

fig,ax = plt.subplots(1, 3)
for i in range(0,len(KS_filepath)):
    KS_file = pd.ExcelFile(KS_filepath[i])
    dfKS = KS_file.parse('Sheet1')
    RPM = [3200,2800,2400,2000,1600,1200]
    dfKS = dfKS.set_index('INCA engine speed (RPM)')
    fig1 = dfKS['Power (kW)'].plot(kind='line',figsize=(20, 6),grid=True,xticks=RPM,ax = ax[0],title='Power',marker='o')
    fig1.set_ylabel('kW')
    fig1.set_xlabel('RPM')
    fig2 = dfKS['Fuel flow (kg/h)'].plot(kind='line',figsize=(20, 6), grid=True,xticks=RPM,ax = ax[1],title='Fuel Flow',marker='o')
    fig2.set_ylabel('kg/h')
    fig2.set_xlabel('RPM')
    fig3 = dfKS['Exh pressure(mbar)'].plot(kind='line',figsize=(20, 6), grid=True,xticks=RPM,ax = ax[2],title='Exhaust pressure',marker='o')
    fig3.set_ylabel('mbar')
    fig3.set_xlabel('RPM')
    fig.legend(lis)
    plt.savefig(os.path.join(folderPath,"WOT_Compare.png"), bbox_inches='tight')