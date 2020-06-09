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

excelfile1 = easygui.fileopenbox(msg='Select dat files', default='*.xlsx', multiple = True)


KS_file = pd.ExcelFile(excelfile1[0])    

ks_file_data = KS_file.parse('Sheet1')

ks_file_data.drop(([0,1]),axis=0,inplace=True)
