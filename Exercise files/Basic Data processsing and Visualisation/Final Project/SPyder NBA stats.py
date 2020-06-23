#Created by: Nikhil Polpakkara
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
import collections
from scipy.stats import rankdata

path = 'D:/NIKHIL/ANACONDA PYTHON/Git repository/Python/Exercise files/Basic Data processsing and Visualisation/Final Project/Dataset/games_details.csv'
df_games = pd.read_csv(path)

No_of_games = [d for d in df_games.groupby('GAME_ID',axis=0)]

# df = df_games.groupby('GAME_ID',axis=0)

# df_Player_stat = df_games.groupby('PLAYER_NAME',axis=0)

    
df = df_games
df = df.set_index('PLAYER_NAME')

Tot_rebounds = defaultdict()
for d in df_games['PLAYER_NAME']:
    Tot_rebounds[d] = +1

list_players = list(Tot_rebounds.keys())

Tot_rebound_ = defaultdict()
for name in list_players:
    Tot_rebound_[name] = df.loc[name]['REB'].sum()


Max_reb = max(Tot_rebound_, key=Tot_rebound_.get)
top_rebounders = [(Tot_rebound_[p],p) for p in Tot_rebound_]
top_rebounders= top_rebounders.sort()
top_rebounders[-5:]

rank = list(range(1,len(top_rebounders)+1))
Reb_rank = defaultdict()
for i in range (0,len(top_rebounders)):
    Reb_rank[top_rebounders[i][1]] = rank[i]

Reb_rank_tup = [(top_rebounders[i][1],rank[i]) for i in range (0,len(top_rebounders))]

Reb_rank = Rank(df_games,'REB')
Pts_rank = Rank(df_games,'PTS')

#%%
def Rank(df_,x):
    df = df_
    df = df.set_index('PLAYER_NAME')
    players = defaultdict()
    for d in df_['PLAYER_NAME']:
        players[d] = +1
    list_players = list(players.keys())
    
    Tot_rebound_ = defaultdict()
    for name in list_players:
        Tot_rebound_[name] = df.loc[name][x].sum()
    
    Max = max(Tot_rebound_, key=Tot_rebound_.get)
    
    ff = dict(zip(Tot_rebound_.keys(), rankdata([-i for i in Tot_rebound_.values()], method='min')))
    rank = [(ff[p],p) for p in ff]
    rank.sort()
    
    rank_dict = {}
    for i in rank:
        rank_dict[i[1]] = i[0]
    
    return rank_dict
#%%
x = {'a':10.1, 'b':2, 'c': 5, 'd': 5, 'e':10.1}
{key: rank for rank, key in enumerate(sorted(x, key=x.get, reverse=True), 1)}

r = {key: rank for rank, key in enumerate(sorted(set(Tot_rebound_.values()), reverse=True), 1)}
dd = {k: r[v] for k,v in Tot_rebound_.items()}

top_rebounders_ = [(dd[p],p) for p in dd]
top_rebounders_.sort()

ll = {key: rank for rank, key in enumerate(sorted(Tot_rebound_, key=Tot_rebound_.get, reverse=True), 1)}

#%%
import operator
x={'a':10.1,'b':2,'c':5,'d': 5, 'e':10.1}
sorted_x = sorted(x.items(), key=operator.itemgetter(1), reverse =True)
out_dict = {}
for idx, (key, _) in enumerate(sorted_x):
    out_dict[key] = idx + 1
print(out_dict)

m = {}
k = 0
for i in dict(sorted(x.items(), key=lambda k: k[1], reverse=True)):
    k += 1
    m[i] = k
    
ff = dict(zip(Tot_rebound_.keys(), rankdata([-i for i in Tot_rebound_.values()], method='min')))
top_rebounders_ = [(ff[p],p) for p in ff]
top_rebounders_.sort()

rank_dict = {}
for i in top_rebounders_:
    rank_dict[i[1]] = i[0]