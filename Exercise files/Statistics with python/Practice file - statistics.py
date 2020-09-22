# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:52:38 2020

@author: nikhilp
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.formula.api as sm

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
#%%
# Grouping
data = pd.DataFrame({
'Gender': ['f', 'f', 'm', 'f', 'm',
'm', 'f', 'm', 'f', 'm', 'm'],
'TV': [3.4, 3.5, 2.6, 4.7, 4.1, 4.1,
5.1, 3.9, 3.7, 2.1, 4.3]
})
# Group the data
grouped = data.groupby('Gender')
# Do some overview statistics
print(grouped.describe())
# Plot the data:
grouped.boxplot(figsize = (10,5))
plt.show()

# Get the groups as DataFrames
df_female = grouped.get_group('f')
# Get the corresponding numpy-array
values_female = grouped.get_group('f').values
values_female = df_female.values
#%%
# Statsmodel
# Generate a noisy line, and save the data in a pandas-DataFrame
x = np.arange(100)
y = 0.5*x - 20 + np.random.randn(len(x))
df = pd.DataFrame({'x':x, 'y':y})

model = sm.ols('y~x', data=df).fit()
print( model.summary() )
#%%
#Seaborn
import seaborn as sns
x = np.linspace(1, 7, 50)
y = 3 + 2*x + 1.5*np.random.randn(len(x))
df = pd.DataFrame({'xData':x, 'yData':y})
plots = sns.regplot('xData', 'yData', data=df,)
plt.show(plots)
#%%
x= np.linspace(0,10,0.1)
y