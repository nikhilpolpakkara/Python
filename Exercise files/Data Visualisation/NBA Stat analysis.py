#Created by: Nikhil Polpakkara
import pandas as pd
import numpy as np

df_nba = pd.read_csv('NBA stats.csv')
df_nba.columns.tolist()

df_nba.set_index('PlayerName',inplace=True)
df_nba.reset_index()
df_nba_player = df_nba.groupby('PlayerName',axis=0).sum()

df_nba_player.head()

df_nba_player.sort_values('PTS',ascending=True,inplace=True)

df_nba_player.replace(['https://www.kaggle.com/drgilermo/nba-players-statshttps:'],[' '])

df_nba_player = df_nba_player.reset_index()
df_nba_player.drop([0],axis=0,inplace=True)
df_nba_player.head()

lis = list(range(1,3922))
player_index = list(df_nba_player.index)
player_column = list(df_nba_player.columns)

df_player_100_plus_G = pd.DataFrame(index=player_index,columns=player_column)
for i in range(1,5):     #len(player_index)+1
    if df_nba_player.loc[i,'G'] >= 100:
        df1 = pd.DataFrame(df_nba_player.loc[i]).transpose()    
    print(df1)
    df_player_100_plus_G.append(df1)
    print(df_player_100_plus_G)
#df_nba_player.rename(columns= lambda x: x.strip(),inplace=True)
df_nba_player.columns = df_nba_player.columns.str.strip()

df = pd.DataFrame([[1, 2], [3, 4]], columns=list('AB'))
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=list('AB'))
df.append(df2)

condition = df_nba_player.loc[lis,'G'] > 100
df_player_100_plus_G = df_nba_player[condition]
df_nba_player.set_index('PlayerName',inplace=True)
df_nba_player.reset_index()
