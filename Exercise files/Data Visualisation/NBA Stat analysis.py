#NBA stats analysis

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


NBA_SS = pd.read_excel('NBA stats.xlsx',sheet_name='NBA stats')

NBA_SS.drop(['#'],axis=1, inplace=True)
NBA_SS.head(5)
NBA_SS.replace(' ',0)

NBA_SS.columns.tolist()
NBA_SS.index.tolist()

peat = list(range(1991,1994))

#NBA_SS.reset_index()
NBA_SS.set_index(['Player Name','Year'],inplace=True)
#NBA_SS.set_index('Player Name',inplace=True)
NBA_SS.sort_values(by='Year', ascending=True, axis=0, inplace=True)
graph = NBA_SS.loc[(['Michael Jordan*','Scottie Pippen*'],peat),'Points']
graph.plot(figsize=(10, 5))

