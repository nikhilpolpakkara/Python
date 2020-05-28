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

modalFilePath = easygui.fileopenbox(msg='Select dat files', default='*.xls', multiple = True)
xlsModalFile = pd.ExcelFile(modalFilePath[0])
dfModal = xlsModalFile.parse('Data')

dfModal['actualSpeed'] = dfModal['ActualSpeed (km/h)\n[km/h]'].values
dfModal['NOx'] = dfModal['NOx_grams (Dil)\n[grams]'].values

dfModal['NOx'].plot(kind='line', figsize=(10, 6), rot=90) 

plt.xlabel('time(s)')
plt.ylabel('NOx(g)')
plt.title('NOx Modal')



dfModal['THC'] = dfModal['THC_grams (Dil)\n[grams]'].values
dfModal['THC'].plot(kind='line', figsize=(10, 6), rot=90) 

plt.xlabel('time(s)')
plt.ylabel('THC(g)')
plt.title('THC Modal')

plt.show()
