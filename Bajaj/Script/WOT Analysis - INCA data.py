# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:04:31 2020

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



datFiles = easygui.fileopenbox(msg='Select dat files', default='*.dat', multiple = True)
#get the folderpath of dat file
folderPath = os.path.dirname(datFiles[0])

def Averaging_df(x,y):
    RPM = [3200,3000,2800,2600,2400,2200,2000,1800,1600,1400,1200]
    # RPM = [3150,2950,2750,2550,2350,2150,1950,1750,1550,1350,1150]
    mean_ = []
    for i in RPM:
        df_i = x[(x['cps_n_engine'] > i-50) & (x['cps_n_engine'] < i+50)]
        a = df_i[y].mean()
        mean_.append(a)
    mean_dict = {'Engine speed (RPM)':RPM,y:mean_}
    df_mean_ = pd.DataFrame(mean_dict)
    df_mean_.set_index(df_mean_['Engine speed (RPM)'])
    # print(df_mean_)
    return df_mean_[y]



def graph_(X,Y):
    RPM = [3400,3200,3000,2800,2600,2400,2200,2000,1800,1600,1400,1200]
    # RPM = [3200,3000,2800,2600,2400,2200,2000,1800,1600,1400,1200]
    # RPM = [3150,2950,2750,2550,2350,2150,1950,1750,1550,1350,1150]
    graph_ = X.plot(x ='INCA engine speed (RPM)' , y = Y,figsize=(10, 6),
                    rot=90,xticks= RPM,kind = 'line',grid=True,marker='o')
    for x,y in zip(RPM,X[Y]):
        graph_.annotate(str(y),xy=(x,y))
    return graph_

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
                     #'egr_T_limiting_temp_low', 'egr_T_limiting_temp_high',
                     'egr_P_exhaustp','egr_P_intakep']#'egr_P_intakep_min','egr_P_intakep']
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
    graphFolderPath = os.path.join(folderPath, baseName)
    if not os.path.exists(graphFolderPath):
        os.mkdir(graphFolderPath)
    
    excelFilePath = os.path.join(graphFolderPath, excelFile)

    df_Eng_spd = round(Averaging_df(df,'cps_n_engine'),0)
    df_Exh_temp = round(Averaging_df(df,'egr_T_exhaust_temperature'),2)
    df_Oil_temp = round(Averaging_df(df,'egr_T_oil_temperature'),2)    
    df_Exh_press = round(Averaging_df(df,'egr_P_exhaustp'),2) 
    df_Intake_press = round(Averaging_df(df,'egr_P_intakep'),2)
    
    df_Average = pd.DataFrame()
    df_Average['INCA engine speed (RPM)'] = df_Eng_spd
    df_Average['Oil temp(°C)'] = df_Oil_temp
    df_Average['Exhaust temp(°C)'] = df_Exh_temp
    df_Average['Exh pressure(mbar)'] = df_Exh_press
    df_Average['Intake pressure(mbar)'] = df_Intake_press
   

    df_Average.to_excel(excelFilePath)
    
    # df_graph = df_Average
    # df_graph.set_index(df_graph['Engine speed (RPM)'])    
    
       
    Intake_pressure = graph_(df_Average,'Intake pressure(mbar)')
    plt.grid(linestyle='dotted')
    plt.xlabel('RPM')
    plt.ylabel('mbar')
    plt.title('Intake Pressure')
    plt.show()
    plt.savefig(os.path.join(graphFolderPath, baseName + "_Intake pressure.png"), bbox_inches='tight')
    
    Exhaust_pressure = graph_(df_Average,'Exh pressure(mbar)')
    plt.grid(linestyle='dotted')
    plt.xlabel('RPM')
    plt.ylabel('mbar')
    plt.title('Exhaust Back Pressure')
    plt.show()
    plt.savefig(os.path.join(graphFolderPath, baseName + "_Exh_press.png"), bbox_inches='tight')
    
    Exhaust_temperature = graph_(df_Average,'Exhaust temp(°C)')
    plt.grid(linestyle='dotted')
    plt.xlabel('RPM')
    plt.ylabel('kg/h')
    plt.title('Exhaust temp(°C)')
    plt.show()
    plt.savefig(os.path.join(graphFolderPath, baseName + "__Exhaust temp.png"), bbox_inches='tight')
    # print('Pressure @ 3200RPM :',df_Average['egr_P_exhaustp'][1])