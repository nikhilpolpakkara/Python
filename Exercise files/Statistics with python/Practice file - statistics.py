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
# Import the required packages
import matplotlib.pyplot as plt
import numpy as np
# Generate the data
x = np.arange(0, 10, 0.2)
y = np.sin(x)
z = np.cos(x)
# Generate the figure and the axes
fig, axs = plt.subplots(nrows=2, ncols=1)
# On the first axis, plot the sine and label the ordinate
axs[0].plot(x,y)
axs[0].set_ylabel('Sine')
# On the second axis, plot the cosine
axs[1].plot(x,z)
axs[1].set_ylabel('Cosine')
# Display the resulting plot
fig.show()
#%%
#KDE Plot
import statistics
x =np.random.randn(100)
sns.kdeplot(x,bw=1)
sd=statistics.stdev(x)
n=len(x)

"""
It can be shown that under certain conditions the optimal choice for h is
h = 1.06*S.D*(n)^(-1/5)
"""
h = 1.06*sd*(n**(-0.2)) # h=0.36789080560138004
sns.kdeplot(x,bw=h)
#%%
# imports specific to the plots in this example
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
# Twice as wide as it is tall.
fig = plt.figure(figsize=plt.figaspect(0.5))
#---- First subplot
# Note that the declaration "projection='3d'"
# is required for 3d plots!
ax = fig.add_subplot(1, 2, 1, projection='3d')
# Generate the grid
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
X, Y = np.meshgrid(X, Y)
# Generate the surface data
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)
# Plot the surface
surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
cmap=cm.GnBu, linewidth=0, antialiased=False)
ax.set_zlim3d(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=10)
#---- Second subplot
ax = fig.add_subplot(1, 2, 2, projection='3d')
X, Y, Z = get_test_data(0.05)
ax.plot_wireframe(X, Y, Z, rstride=10, cstride=10)
outfile = '3dGraph.png'
plt.savefig(outfile, dpi=200)
print('Image saved to {0}'.format(outfile))
plt.show()