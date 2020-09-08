# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 16:30:04 2020

@author: nikhilp
"""

import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime
from IPython.display import display, Markdown
import seaborn as sns
from math import pi
import collections
from scipy.stats import rankdata


path = 'D:/NIKHIL/ANACONDA PYTHON/Git repository/Python/Exercise files/Basic Data processsing and Visualisation/Final Project/Dataset/games_details.csv'
#path = 'M:/Git repository/Python/Exercise files/Basic Data processsing and Visualisation/Final Project/Dataset/games_details.csv'
path_2 = 'D:/NIKHIL/ANACONDA PYTHON/Git repository/Python/Exercise files/Basic Data processsing and Visualisation/Final Project/Dataset/games.csv'
#path_2 = 'M:/Git repository/Python/Exercise files/Basic Data processsing and Visualisation/Final Project/Dataset/games.csv'
df_games1 = pd.read_csv(path)
df_gms = pd.read_csv(path_2)
df_gms.head()

nullvals = df_games1.isnull().sum()
nullvals.plot(kind='bar')
plt.ylabel('No: of missing data')
plt.title('Missing data')

df_games1 = df_games1.fillna(0)
nullvals = df_games1.isnull().sum()

condition = df_gms['SEASON'] > 2010
df_gms_decade_2020 = df_gms[condition]

df_win_team = {}
for ind in df_gms.index:
    if df_gms['HOME_TEAM_WINS'][ind] >0:
        df_win_team[df_gms['GAME_ID'][ind]] = df_gms['TEAM_ID_home'][ind]
    else:
        df_win_team[df_gms['GAME_ID'][ind]] = df_gms['TEAM_ID_away'][ind]
df_games1['WIN_TEAM_ID'] = df_games1['GAME_ID'].map(df_win_team)

#%%
df = df_games1[df_games1['GAME_ID'].isin(df_gms_decade_2020['GAME_ID'])]
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
    #rank = rank[:100]
    
    rank_dict = {}
    for i in rank:
        rank_dict[i[1]] = i[0]
    
    return rank_dict
def dict_to_tup(dict_):
    list_tup =[(dict_[p],p) for p in dict_]
    return list_tup.sort()

def NO_of_win(rank,df_,df2):
    player_win = {}
    for i in range(0,16):                    
        cond_1 = df_['PLAYER_NAME'] == rank[i][1]
        df_player_win = df_[cond_1]
    
        wins = 0
        for ind in df_player_win.index:
            if df_player_win['TEAM_ID'][ind] == df_player_win['WIN_TEAM_ID'][ind]:
                wins = wins + 1
        player_win[rank[i][1]] = wins
    return player_win

def ranking_dict(v1,v2,v3):
    new_dict = {}
    for i,j in v1.items():
        for x,y in v2.items():
            for a,b in v3.items():
                if i==x==a:
                    new_dict[i]=j+y+b
    new_rank = [(new_dict[p],p) for p in new_dict]
    new_rank.sort()
    return new_rank
#%%
Reb_rank = Rank(df,'REB')
DReb_rank = Rank(df,'DREB')
OReb_rank = Rank(df,'OREB')
Pts_rank = Rank(df,'PTS')
Ast_rank = Rank(df,'AST')
Stl_rank = Rank(df,'STL')
Blk_rank = Rank(df,'BLK')
FG_pct_rank = Rank(df,'FG_PCT')
FG3_pct_rank = Rank(df,'FG3_PCT')
#%%
                                        #DEFENSIVE BEAST

defensive_list = ranking_dict(DReb_rank,Blk_rank,Stl_rank)
defensive_list[:5]
     
df_Defensive_beast = pd.DataFrame(columns=['PLAYER_NAME', 'TOT_DREB', 'TOT_STL','TOT_BLK'])
pl_nme = []
tot_dreb = []
tot_stl = []
tot_blk = []
for rank,player in defensive_list[:5]:
    PL = df['PLAYER_NAME'] == player
    df_player = df[PL]
    pl_nme.append(player)
    tot_dreb.append(df_player['DREB'].sum())
    tot_stl.append(df_player['STL'].sum())
    tot_blk.append(df_player['BLK'].sum())
    
df_Defensive_beast['PLAYER_NAME'] = pl_nme
df_Defensive_beast['TOT_DREB'] = tot_dreb
df_Defensive_beast['TOT_STL'] = tot_stl
df_Defensive_beast['TOT_BLK'] = tot_blk

df_Defensive_beast.set_index('PLAYER_NAME')

fig,ax = plt.subplots(1,3) 
fig1 = df_Defensive_beast['TOT_DREB'].plot(kind='bar',ax=ax[0],title='Defensive rebounds',figsize=(15, 5))
fig1.set_ylabel('Total rebounds')
fig2 = df_Defensive_beast['TOT_STL'].plot(kind='bar',ax=ax[1],title='Steals',figsize=(15, 5))
fig2.set_ylabel('Steals')
fig3 = df_Defensive_beast['TOT_BLK'].plot(kind='bar',ax=ax[2],title='Blocks',figsize=(15, 5))
fig3.set_ylabel('Blocks')

player_wins = NO_of_win(defensive_list,df,df_gms_decade_2020)
df_Defensive_beast['TOT_WINS'] = df_Defensive_beast['PLAYER_NAME'].map(player_wins)
df_Defensive_beast
#%%
top_10_Reb = list(n for n,i in Reb_rank.items())[:10]
top_10_Pts = list(n for n,i in Pts_rank.items())[:10]
top_10_ast = list(n for n,i in Ast_rank.items())[:10]
top_10_Stl = list(n for n,i in Stl_rank.items())[:10]
top_10_Blk = list(n for n,i in Blk_rank.items())[:10]
df_Best_player = pd.DataFrame(columns=['REB rank', 'PTS rank', 'STL rank','BLK rank','AST rank'])
df_Best_player['REB rank'] = top_10_Reb
df_Best_player['PTS rank'] = top_10_Pts
df_Best_player['STL rank'] = top_10_ast
df_Best_player['BLK rank'] = top_10_Stl
df_Best_player['AST rank'] = top_10_Blk

z = new_ranking_dict(Reb_rank,Pts_rank,Ast_rank,Stl_rank,Blk_rank)

#%%
def new_ranking_dict(v1,v2,v3,v4,v5):
    new_dict = {}
    for i,j in v1.items():
        for x,y in v2.items():
            for a,b in v3.items():
                for g,f in v4.items():
                    for k,l in v5.items():
                        if i==x==a==g==k:
                            new_dict[i]=j+y+b+f+l
    new_rank = [(new_dict[p],p) for p in new_dict]
    new_rank.sort()
    return new_rank
#%%
#  Player efficiency i- ((PTS + REB + AST + STL + BLK − Missed FG − Missed FT - TO) / GP)
pl_nme = []
tot_dreb_e = []
tot_pts_e = []
tot_stl_e = []
tot_blk_e = []
tot_ast_e = []
tot_missed_fg_e = []
tot_missed_ft_e = []
tot_TO = []
    
for i in z:
    for ind in df.index:
        if df['PLAYER_NAME'][ind] = i[1]:
            PL_e = df['PLAYER_NAME'][ind] == player
            df_playe_e = df[PL_e]
            tot_pts_e.append(df_player['PTS'].sum())
            tot_dreb_e.append(df_player['DREB'].sum())
            tot_stl_e.append(df_player['STL'].sum())
            tot_blk_e.append(df_player['BLK'].sum())
            tot_ast_e.append(df_player['AST'].sum())
            tot_missed_fg_e.append(df_player['FGA'].sum()-df_player['FGM'].sum())
            tot_missed_ft_e.append(df_player['FTA'].sum()-df_player['FTM'].sum())
            tot_TO.append(df_player['PTS'].sum())


cc=list(df_games1['MIN'][100])

time_list = []

for ind in cc:
    if type(ind) == str:
        try:
            pt = datetime.strptime(ind,'%M:%S')
            total_seconds = pt.second + pt.minute*60
            time_list.append(total_seconds)
        except:
            print('warning')
    else:
        time_list.append(ind)

df_games1['TIME_PLAYED']= time_list    


word = 'bad:00'

word[:-3].strip()

for ind in df_games1.index:
    if df_games1['MIN'][ind] == str:
        if len(df_games1['MIN'][ind])>5:
            df_games1['MIN'][ind] = df_games1['MIN'][ind][:-3].strip()





