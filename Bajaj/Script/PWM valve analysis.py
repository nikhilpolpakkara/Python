# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:52:29 2020

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
import openpyxl

def Averaging_df(x,y):
    EGR_Flow_perc = [0,2,4,6,8,10,12,14,16,18,20]
    sl_no = [1,2,3,4,5,6,7,8,9,10,11]
    mean_ = []
    for i in EGR_Flow_perc:
        df_i = x[(x['egr_pct_req_flow'] > i-0.5) & (x['egr_pct_req_flow'] < i+0.5)]
        a = df_i[y].mean()
        mean_.append(a)
    mean_dict = {'sl.no':sl_no,'egr_pct_req_flow': EGR_Flow_perc,y:mean_}
    df_mean_ = pd.DataFrame(mean_dict)
    df_mean_ = df_mean_.set_index(df_mean_['sl.no'])
    # print(df_mean_)
    return df_mean_[y]

#Reading INCA data

#asks the dat file from user
datFiles = easygui.fileopenbox(msg='Select dat files', default='*.dat', multiple = True)
#get the folderpath of dat file
folderPath = os.path.dirname(datFiles[0])
#dictionary of dataframes
dfs = {}
for datFile in datFiles:
    #get the basename of the file 
    baseName = os.path.basename(datFile)[:-4]
#    modalFileName = baseName + ".xls"
#    modalFilePath = os.path.join(folderPath, modalFileName)
    #create directory to store all the plots
    graphFolderPath = os.path.join(folderPath, baseName)
    if not os.path.exists(graphFolderPath):
        os.mkdir(graphFolderPath)
#   xlsModalFile = pd.ExcelFile(modalFilePath)
    #reading the modal data
#    dfModal = xlsModalFile.parse('Data')
    #reading the mdf file
    mdf = MDF(datFile)
    #getting all signals in mdf object
    allSignals = list(mdf.channels_db.keys())
    measuredSignals = []
    #remove signals with CPP in it
    for signal in allSignals:
        if not(("CCP" in signal) or ("_sword" in signal) or "$" in signal):
            measuredSignals.append(signal)
    #creating an empty list of important signals
    impSignals = ['cps_n_engine','egr_pct_req_flow','egr_mm_Target_Pos','egr_mm_Current_Pos',
                      'egr_T_exhaust_temperature', 'egr_T_oil_temperature',
                      'egr_kghr_egr_flow_req','egr_kghr_egr_flow_th','egr_kghr_intake_flow_act',
                      'egr_P_deltap_cycle','egr_P_deltap_inst',
                      'egr_P_exhaustp']
                      #,'egr_P_intakep_min','egr_P_intakep']
    df = mdf.to_dataframe(
            channels=impSignals,
            raster= 'egr_pct_req_flow',
            time_from_zero=True,
            empty_channels="zeros",
#            keep_arrays=False,
            use_display_names=True,
            time_as_date=True,
            reduce_memory_usage=True,
            raw=False,
            ignore_value2text_conversions=False)
    #remove \CCP from column names of dataframe
    df.columns = [col.split('\\')[0] for col in df.columns]
    #resampling the data to 1 second
    df = df.resample('S').mean()
    df = df.round(1)
    sl_no = list(range(1,len(df)+1))
    df['sl.no'] = sl_no
    df = df.set_index('sl.no')
    mdf.close()
    df.fillna(0, inplace = True)
    columnOrderExcel = impSignals
    excelFile = baseName + '_data.xlsx'
    excelFilePath = os.path.join(graphFolderPath, excelFile)
    
    
    df_Avg = pd.DataFrame()

    for i in impSignals:
        a = Averaging_df(df,i)
        # print(a)
        df_Avg[i] = a
    df_Avg['Error in lift'] = df['egr_mm_Target_Pos']-df['egr_mm_Current_Pos']
    df_Avg.to_excel(excelFilePath, columns = columnOrderExcel)
