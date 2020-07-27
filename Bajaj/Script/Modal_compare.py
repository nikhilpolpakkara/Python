# -*- coding: utf-8 -*-
"""
Created on Tue May 26 16:51:59 2020

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



modalFilePath1 = easygui.fileopenbox(msg='Select dat files', default='*.xls', multiple = True)
#folderPath = os.path.dirname(modalFilePath1[0])

lis = []
for i in range(0,len(modalFilePath1)):
    a = input("Enter Legend") #for",i,'st Modal')

    lis.append(a)


    

def Subplot_NOx():    
    fig,ax = plt.subplots(2, 3)
    for i in range(0,len(modalFilePath1)):
        xlsModalFile = pd.ExcelFile(modalFilePath1[i])
        dfModal = xlsModalFile.parse('Data')
        dfModal['NOx'] = dfModal['NOx_grams (Dil)\n[grams]'].values*1000
        fig1 = dfModal['NOx'][0:109].plot(kind='line',figsize=(15, 6), grid=True,ax = ax[0,0])
        fig1.set_ylabel('mg')
        fig1.title.set_text('1st cycle')
        fig2 = dfModal['NOx'][109:217].plot(kind='line',figsize=(15, 6), grid=True,ax = ax[0,1])
        fig2.title.set_text('2nd cycle')
        fig3 = dfModal['NOx'][217:325].plot(kind='line',figsize=(15, 6),grid=True,ax = ax[0,2])
        fig3.title.set_text('3rd cycle')
        fig4 = dfModal['NOx'][325:432].plot(kind='line',figsize=(15, 6), grid=True,ax = ax[1,0])
        fig4.set_xlabel('time(s)')
        fig4.set_ylabel('mg')
        fig4.title.set_text('4th cycle')
        fig5 = dfModal['NOx'][432:541].plot(kind='line',figsize=(15, 6), grid=True,ax = ax[1,1])
        fig5.set_xlabel('time(s)')
        fig5.title.set_text('5th cycle')
        fig6 = dfModal['NOx'][541:649].plot(kind='line',figsize=(15, 6),grid=True,ax = ax[1,2])
        fig6.set_xlabel('time(s)')
        fig6.title.set_text('6th cycle')
        fig.legend(lis)
        fig.suptitle('NOx Modal')

def Subplot_THC():    
    fig,ax = plt.subplots(2, 3)
    for i in range(0,len(modalFilePath1)):
        xlsModalFile = pd.ExcelFile(modalFilePath1[i])
        dfModal = xlsModalFile.parse('Data')
        dfModal['THC'] = dfModal['THC_grams (Dil)\n[grams]'].values*1000
        fig1 = dfModal['THC'][0:109].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[0,0])
        fig1.set_ylabel('mg')
        fig2 = dfModal['THC'][109:217].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[0,1])
        fig3 = dfModal['THC'][217:325].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[0,2])
        fig4 = dfModal['THC'][325:432].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[1,0])
        fig4.set_xlabel('time(s)')
        fig4.set_ylabel('mg')
        fig5 = dfModal['THC'][432:541].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[1,1])
        fig5.set_xlabel('time(s)')
        fig6 = dfModal['THC'][541:649].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[1,2])
        fig6.set_xlabel('time(s)')
        fig.legend(lis)
        fig.suptitle('THC Modal')

def Subplot_CO():    
    fig,ax = plt.subplots(2, 3)
    for i in range(0,len(modalFilePath1)):
        xlsModalFile = pd.ExcelFile(modalFilePath1[i])
        dfModal = xlsModalFile.parse('Data')
        dfModal['CO'] = dfModal['CO_grams (Dil)\n[grams]'].values*1000
        fig1 = dfModal['CO'][0:109].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[0,0])
        fig1.set_ylabel('mg')
        fig2 = dfModal['CO'][109:217].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[0,1])
        fig3 = dfModal['CO'][217:325].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[0,2])
        fig4 = dfModal['CO'][325:432].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[1,0])
        fig4.set_xlabel('time(s)')
        fig4.set_ylabel('mg')
        fig5 = dfModal['CO'][432:541].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[1,1])
        fig5.set_xlabel('time(s)')
        fig6 = dfModal['CO'][541:649].plot(kind='line',figsize=(15, 6), rot=90,grid=True,ax = ax[1,2])
        fig6.set_xlabel('time(s)')
        fig.legend(lis)
        fig.suptitle('CO Modal')

def graph(x):
    xtick = [108,216,324,432,540,648,756]
    graph_ = x.plot(kind='line',figsize=(10, 6), rot=90,xticks=xtick,grid=True,legend=True) 
    graph_.legend(lis)
    plt.grid(linestyle='dotted')
    plt.xlabel('time(s)')
    plt.ylabel('mg')
    plt.title(x.name+" Modal")
    
def Modal_graph(modalFilePath):
#    lis = []
    for i in range(0,len(modalFilePath1)):
        xlsModalFile = pd.ExcelFile(modalFilePath[i])
        dfModal = xlsModalFile.parse('Data')
#        dfModal['actualSpeed'] = dfModal['ActualSpeed (km/h)\n[km/h]'].values
        dfModal['NOx'] = dfModal['NOx_grams (Dil)\n[grams]'].values*1000
        graph(dfModal['NOx'])
    plt.figure()
        
    for i in range(0,len(modalFilePath1)):
        xlsModalFile = pd.ExcelFile(modalFilePath[i])
        dfModal = xlsModalFile.parse('Data')
        dfModal['CO'] = dfModal['CO_grams (Dil)\n[grams]'].values*1000
        graph(dfModal['CO'])
    plt.figure()
    
    for i in range(0,len(modalFilePath1)):
        xlsModalFile = pd.ExcelFile(modalFilePath[i])
        dfModal = xlsModalFile.parse('Data')
        dfModal['THC'] = dfModal['THC_grams (Dil)\n[grams]'].values*1000
        graph(dfModal['THC'])
    
#        dfModal['THC'] = dfModal['THC_grams (Dil)\n[grams]'].values
#        dfModal['CO'] = dfModal['CO_grams (Dil)\n[grams]'].values
#        NOx_modal = graph(dfModal['NOx'])
#        plt.show()
#        CO_modal = graph(dfModal['CO'])
#        plt.show()
#        THC_modal = graph(dfModal['HC'])   
#        plt.show()
#    plt.show()
#    plt.savefig(os.path.join(graphFolderPath, baseName + "__binnedAvgNOx.png"), bbox_inches='tight')
"""
dfModal['THC'] = dfModal['THC_grams (Dil)\n[grams]'].values
dfModal['THC'].plot(kind='line', figsize=(10, 6), rot=90) 
plt.xlabel('time(s)')
plt.ylabel('THC(g)')
plt.title('THC Modal')
"""
try:
    Modal_graph(modalFilePath1)
except:
    print('No file')  
Subplot_NOx()
Subplot_THC()
Subplot_CO()


