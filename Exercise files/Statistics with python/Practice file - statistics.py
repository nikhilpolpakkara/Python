# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:52:38 2020

@author: nikhilp
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0,10,0.1)
x = np.sin(t)
y = np.cos(t)
df = pd.DataFrame({'Time':t, 'x':x, 'y':y})
a = df['x']
a.plot()

for i in range(0,5):
    aa = df[0:i]

df= df.set_index('Time')

lis = a
df['Name'] = lis