# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:29:11 2020

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
#%%
datFiles = easygui.fileopenbox(msg='Select dat files', default='*.dat', multiple = True)
#get the folderpath of dat file
folderPath = os.path.dirname(datFiles[0])

#def read_df():
dfs = {}
for datFile in datFiles:
    mdf = MDF(datFile)
    allSignals = list(mdf.channels_db.keys())
    measuredSignals = []
    #remove signals with CPP in it
    for signal in allSignals:
        if not(("CCP" in signal) or ("_sword" in signal) or "$" in signal):
            measuredSignals.append(signal)
    #creating an empty list of important signals
    impSignals = ['cps_n_engine', 'egr_b_operate_valve', 
                  'egr_T_exhaust_temperature', 'egr_T_oil_temperature',
                  'egr_T_limiting_temp_low', 'egr_T_limiting_temp_high',
                  'egr_P_exhaustp']
    df = mdf.to_dataframe(
            channels=impSignals,
            raster= 'egr_b_operate_valve',
            time_from_zero=True,
            empty_channels="zeros",
#               keep_arrays=False,
            use_display_names=True,
            time_as_date=True,
            reduce_memory_usage=True,
            raw=False,
            ignore_value2text_conversions=False)
    #remove \CCP from column names of dataframe
    df.columns = [col.split('\\')[0] for col in df.columns]
    #resampling the data to 1 second
    df = df.resample('S').mean()
    
    n_i = list(range(1,len(df['egr_b_operate_valve'])+1))
    df['Sl.no'] = n_i
    df.set_index('Sl.no',inplace=True)

    mdf.close()
    

#%%
def exh_pressure_sampling():
    
    RPM = [3400,3200,3000,2800,2600,2400,2200,2000,1800,1600,1400,1200]
    mean_pres = []
    for i in RPM:
        df_i = df[(df['cps_n_engine'] > i-50) & (df['cps_n_engine'] < i+50)]
        a = df_i['egr_P_exhaustp'].mean()
        mean_pres.append(a)
    pres_dict = {'Engine Speed':RPM,'Mean Pressure':mean_pres}
    df_mean_pres = pd.DataFrame(pres_dict)
    df_mean_pres.set_index(df_mean_pres['Engine Speed'])
    df_mean_pres.plot(x='Engine Speed',y='Mean Pressure',xticks= RPM,kind = 'line',grid=True)
    plt.grid(linestyle='dotted')
    plt.xlabel('RPM')
    plt.ylabel('mbar')
    plt.title('Exhaust Back Pressure')
    plt.show()
        df_3400_RPM = df[(df['cps_n_engine'] > 3350) & (df['cps_n_engine'] < 3450)]
        df_3200_RPM = df[(df['cps_n_engine'] > 3150) & (df['cps_n_engine'] < 3250)]
        df_3000_RPM = df[(df['cps_n_engine'] > 2950) & (df['cps_n_engine'] < 3050)]
        df_2800_RPM = df[(df['cps_n_engine'] > 2750) & (df['cps_n_engine'] < 2850)]
        df_2600_RPM = df[(df['cps_n_engine'] > 2550) & (df['cps_n_engine'] < 2650)]
        df_2400_RPM = df[(df['cps_n_engine'] > 2350) & (df['cps_n_engine'] < 2450)]
        df_2200_RPM = df[(df['cps_n_engine'] > 2150) & (df['cps_n_engine'] < 2250)]
        df_2000_RPM = df[(df['cps_n_engine'] > 1950) & (df['cps_n_engine'] < 2050)]
        df_1800_RPM = df[(df['cps_n_engine'] > 1750) & (df['cps_n_engine'] < 1850)]
        df_1600_RPM = df[(df['cps_n_engine'] > 1550) & (df['cps_n_engine'] < 1650)]
        df_1400_RPM = df[(df['cps_n_engine'] > 1350) & (df['cps_n_engine'] < 1450)]
        df_1200_RPM = df[(df['cps_n_engine'] > 1150) & (df['cps_n_engine'] < 1250)]
        
        print(df_3400_RPM['egr_P_exhaustp'].mean())
        print(df_3200_RPM['egr_P_exhaustp'].mean())
        print(df_3000_RPM['egr_P_exhaustp'].mean())
        print(df_2800_RPM['egr_P_exhaustp'].mean())
        print(df_2600_RPM['egr_P_exhaustp'].mean())
        print(df_2400_RPM['egr_P_exhaustp'].mean())
        print(df_2200_RPM['egr_P_exhaustp'].mean())
        print(df_2000_RPM['egr_P_exhaustp'].mean())
        print(df_1800_RPM['egr_P_exhaustp'].mean())
        print(df_1400_RPM['egr_P_exhaustp'].mean())
        print(df_1200_RPM['egr_P_exhaustp'].mean())
#%%
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

datFiles = easygui.fileopenbox(msg='Select dat files', default='*.dat', multiple = True)
#get the folderpath of dat file
folderPath = os.path.dirname(datFiles[0])



def Pressure_df(x):
    RPM = [3400,3200,3000,2800,2600,2400,2200,2000,1800,1600,1400,1200]
    mean_pres = []
    for i in RPM:
        df_i = x[(x['cps_n_engine'] > i-50) & (x['cps_n_engine'] < i+50)]
        a = df_i['egr_P_exhaustp'].mean()
        mean_pres.append(a)
    pres_dict = {'Engine Speed':RPM,'Mean Pressure':mean_pres}
    df_mean_pres = pd.DataFrame(pres_dict)
    df_mean_pres.set_index(df_mean_pres['Engine Speed'])
    graph_ = df_mean_pres.plot(x='Engine Speed',y='Mean Pressure',xticks= RPM,kind = 'line',grid=True)
    print(df_mean_pres)
    return df_mean_pres

#def read_df():
dfs = {}
for datFile in datFiles:
    baseName = os.path.basename(datFile)[:-4]
    mdf = MDF(datFile)
    allSignals = list(mdf.channels_db.keys())
    measuredSignals = []
    #remove signals with CPP in it
    for signal in allSignals:
        if not(("CCP" in signal) or ("_sword" in signal) or "$" in signal):
            measuredSignals.append(signal)
        #creating an empty list of important signals
    impSignals = ['cps_n_engine', 'egr_b_operate_valve', 
                     'egr_T_exhaust_temperature', 'egr_T_oil_temperature',
                     'egr_T_limiting_temp_low', 'egr_T_limiting_temp_high',
                     'egr_P_exhaustp']
    df = mdf.to_dataframe(
            channels=impSignals,
            raster= 'egr_b_operate_valve',
            time_from_zero=True,
            empty_channels="zeros",
    #              keep_arrays=False,
            use_display_names=True,
            time_as_date=True,
            reduce_memory_usage=True,
            raw=False,
            ignore_value2text_conversions=False)
    #remove \CCP from column names of dataframe
    df.columns = [col.split('\\')[0] for col in df.columns]
    #resampling the data to 1 second
    df = df.resample('S').mean()
        
    n_i = list(range(1,len(df['egr_b_operate_valve'])+1))
    df['Sl.no'] = n_i
    df.set_index('Sl.no',inplace=True)
    mdf.close()
    
    columnOrderExcel = impSignals
    excelFile = baseName + "WOT.xlsx"
    #df_pressure = pd.DataFrame.append(df)
    baseName = os.path.basename(datFile)[:-4]
    graphFolderPath = os.path.join(folderPath, baseName)
    if not os.path.exists(graphFolderPath):
        os.mkdir(graphFolderPath)
    
    excelFilePath = os.path.join(graphFolderPath, excelFile)
    df.to_excel(excelFilePath, columns = columnOrderExcel)
    
    # Pressure_df(df)
    # plt.grid(linestyle='dotted')
    # plt.xlabel('RPM')
    # plt.ylabel('mbar')
    # plt.title('Exhaust Back Pressure')
    # plt.show()
    
"""    
def graph(x,a,b)
    graph_ = x.plot(x='a',y='b',xticks= RPM,kind = 'line',grid=True)
    plt.grid(linestyle='dotted')
    plt.xlabel('RPM')
    plt.ylabel('mbar')
    plt.title('Exhaust Back Pressure')
"""   

def Averaging_df(x,y):
    RPM = [3400,3200,3000,2800,2600,2400,2200,2000,1800,1600,1400,1200]
    mean_ = []
    for i in RPM:
        df_i = x[(x['cps_n_engine'] > i-50) & (x['cps_n_engine'] < i+50)]
        a = df_i[y].mean()
        mean_.append(a)
    mean_dict = {'Engine Speed':RPM,y:mean_}
    df_mean_ = pd.DataFrame(mean_dict)
    df_mean_.set_index(df_mean_['Engine Speed'])
    # print(df_mean_)
    return df_mean_

Signals = ['cps_n_engine', 'egr_b_operate_valve', 
                     'egr_T_exhaust_temperature', 'egr_T_oil_temperature',
                     #'egr_T_limiting_temp_low', 'egr_T_limiting_temp_high',
                     'egr_P_exhaustp''egr_P_intakep']

df_Exh_temp = Averaging_df(df,'egr_T_exhaust_temperature')
df_Oil_temp = Averaging_df(df,'egr_T_oil_temperature')    
df_Exh_press = Averaging_df(df,'egr_P_exhaustp') 

df_Average = df_Exh_temp.join((df_Oil_temp['egr_T_oil_temperature'],df_Exh_press['egr_P_exhaustp']))
df_Average.to_excel(excelFilePath)


#%%
RPM = [3400,3200,3000,2800,2600,2400,2200,2000,1800,1600,1400,1200]
mean_ = []
for i in RPM:
    df_i = df[(df['cps_n_engine'] > i-50) & (df['cps_n_engine'] < i+50)]
    a = df_i['egr_P_exhaustp'].mean()
    mean_.append(a)
mean_dict = {'Engine Speed':RPM,'egr_P_exhaustp':mean_}
df_mean_ = pd.DataFrame(mean_dict)
df_mean_.set_index(df_mean_['Engine Speed'])
print(df_mean_)