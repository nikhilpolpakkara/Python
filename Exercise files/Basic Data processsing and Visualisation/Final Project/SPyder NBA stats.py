#Created by: Nikhil Polpakkara
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
import collections
from scipy.stats import rankdata

path = 'M:\Git repository\Python\Exercise files\Basic Data processsing and Visualisation\Final Project\Dataset\games_details.csv'
path_2 = 'M:\Git repository\Python\Exercise files\Basic Data processsing and Visualisation\Final Project\Dataset\games.csv'
df_games = pd.read_csv(path)
df_gms = pd.read_csv(path_2)

condition = df_gms['SEASON'] > 2010
df_gms_decade_2020 = df_gms[condition]

gms_ID_dcd_2020 = [df_gms_decade_2020['GAME_ID']]

#No_of_games = [d for d in df_games.groupby('GAME_ID',axis=0)]

# df = df_games.groupby('GAME_ID',axis=0)

# df_Player_stat = df_games.groupby('PLAYER_NAME',axis=0)

df = df_games[df_games['GAME_ID'].isin(df_gms_decade_2020['GAME_ID'])]


Reb_rank = Rank(df,'REB')
DReb_rank = Rank(df,'DREB')
OReb_rank = Rank(df,'OREB')
Pts_rank = Rank(df,'PTS')
Ast_rank = Rank(df,'AST')
Stl_rank = Rank(df,'STL')
Blk_rank = Rank(df,'BLK')

#%%
stl_blk = {}
for x,y in Blk_rank.items():
    for a,b in Stl_rank.items():
        if x==a:
            stl_blk[x]= y+b
stl_blk = [(stl_blk[p],p) for p in stl_blk]
stl_blk.sort()
stl_blk
#%%
new_dict = {}
for i,j in DReb_rank.items():
    for x,y in Blk_rank.items():
        for a,b in Stl_rank.items():
            if i==x==a:
                new_dict[i]=j+y+b
new_rank = [(new_dict[p],p) for p in new_dict]
new_rank.sort()
new_rank


#%%
def dict_to_tup(dict_):
    list_tup =[(dict_[p],p) for p in dict_]
    return list_tup.sort()
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
    rank = rank[:100]
    
    rank_dict = {}
    for i in rank:
        rank_dict[i[1]] = i[0]
    
    return rank_dict
#%%
#Defensive player of the 
#%%
df_win_team = []
if df_gms_decade_2020['HOME_TEAM_WINS'] >0:
    df_win_team.append(df_gms_decade_2020['TEAM_ID_home'])
else:
    df_win_team.append(df_gms_decade_2020['TEAM_ID_away'])
    
lis = list(range(0,len(df_gms_decade_2020['TEAM_ID_home'])))

df_win_tm = [df_gms_decade_2020['TEAM_ID_home'] for  if df_gms_decade_2020['HOME_TEAM_WINS']>0]

condition_home_win = df_gms_decade_2020['HOME_TEAM_WINS'] >0
condition_away_win = df_gms_decade_2020['HOME_TEAM_WINS'] == 0
df_h = df_gms_decade_2020[condition_home_win]
df_a = df_gms_decade_2020[condition_away_win]

df_win_team = {}
for ind in df_gms_decade_2020.index:
    if df_gms_decade_2020['HOME_TEAM_WINS'][ind] >0:
        df_win_team[df_gms_decade_2020['GAME_ID'][ind]] 
        = df_gms_decade_2020['TEAM_ID_home'][ind]
    else:
        df_win_team[df_gms_decade_2020['GAME_ID'][ind]] 
        = df_gms_decade_2020['TEAM_ID_away'][ind]
 
player_win = {}      
for i in new_rank[:15]:
    for ind in df.index:
        player_team_id[]
                    