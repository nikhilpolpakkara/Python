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
#try:
#    Modal_graph(modalFilePath2)
#except:
#    print('No file')   
#try:
#    Modal_graph(modalFilePath3)
#except:
#    print('No file')   

