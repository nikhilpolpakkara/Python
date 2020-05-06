# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 18:30:56 2019

@author: CS
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

def binplotToDataFrame(binplot, xedges, yedges):
    """
    Gives a dataframe from binplot
    """
    
    binplot = binplot.T
    binplot = binplot[::-1]
    #xmid = xedges[:-1] + (xedges[1] - xedges[0])/2
    #ymid = yedges[:-1] + (yedges[1] - yedges[0])/2
    xmid = list(zip(xedges[:-1], xedges[1:]))
    ymid = list(zip(yedges[:-1], yedges[1:]))
    ymid = ymid[::-1]
    binplotdf = pd.DataFrame(binplot)
    binplotdf.columns = xmid
    binplotdf.index = ymid
    return binplotdf

if __name__ == "__main__":
    #asks the dat file from user
    datFile = easygui.fileopenbox(msg='select the file', default='*.dat')
    #converts dat file to mdf object
    mdf = MDF(datFile)
    #exports dat file to mf4 dile
    mdf.convert('4.10').save(datFile,overwrite=True)
    mf4file = datFile[:-3] + "mf4"
    #converts mf4 file to mdf object
    mdf=MDF(mf4file)
    #create name for excel file to be stored
    excelFile = datFile[:-3] + ".xlsx"
    #getting all signals in mdf object
    allSignals = list(mdf.channels_db.keys())
    #creating an empty list of important signals
    impSignals = []
    for signal in allSignals:
        #removing all signals with "_sword" in them
        if "_sword" not in signal:
            impSignals.append(signal)
    #convert mdf object to pandas dataframe
    df = mdf.to_dataframe(
        channels=impSignals,
        raster="egr_b_operate_valve\\CCP:1",
        time_from_zero=True,
        empty_channels="zeros",
        keep_arrays=False,
        use_display_names=True,
        time_as_date=True,
        reduce_memory_usage=False,
        raw=True,
        ignore_value2text_conversions=False)
    #remove \CCP from column names of dataframe
    df.columns = [col.split('\\')[0] for col in df.columns]
    #create rpm and exhaust temeprature bins
    rpmbins = range(1000, 3700, 200)
    exhTbins = range(0, 801, 50)
    #binning by mean of exhaust pressure
    binplot, xedges, yedges, binIndex = binned_statistic_2d(df.cps_n_engine, 
                                                            df.egr_T_exhaust_temperature, df.egr_P_exhaustp/10, statistic= "mean", bins=(rpmbins,exhTbins))
    #removing all the nan values
    binplot[np.isnan(binplot)] = 0
    #get datafrome from binned values
    binplotdf1 = binplotToDataFrame(binplot, xedges, yedges )    
    
    plt.figure()
    #plot heat map of binned values
    ax1 = sns.heatmap(binplotdf1, annot=True, fmt="0.1f", cmap="YlGnBu")
    ax1.set_title("Average exhaust pressure at RPM and exhaust temperature bin")

    #binning of time spent at given RPM and exhaust temperature bins
    binplot, xedges, yedges, binIndex = binned_statistic_2d(df.cps_n_engine, 
                                                            df.egr_T_exhaust_temperature, df.egr_P_exhaustp/10, statistic= "count", bins=(rpmbins,exhTbins))
    binplot[np.isnan(binplot)] = 0
    #converting time to % of time
    binplot = binplot/np.cumsum(binplot)[-1]*100
    #create dataframe for %time at various RPM and exhaust temperature
    binplotdf2 = binplotToDataFrame(binplot, xedges, yedges )
    plt.figure()
    ax2 = sns.heatmap(binplotdf2, annot=True, fmt="0.1f", cmap="YlGnBu")
    ax2.set_title("% time spent at RPM and exhaust temperature bin")
    #writting the binned values in excel file
    with pd.ExcelWriter(excelFile, engine='openpyxl', mode='a') as writer:
        binplotdf1.to_excel(writer,sheet_name='MeanExhaustPressureBinning')
        binplotdf2.to_excel(writer,sheet_name='RPMExhaustTBinning')
        writer.save()
    #closing the excel file
    writer.close()
    mdf.close()
    os.remove(mf4file)
