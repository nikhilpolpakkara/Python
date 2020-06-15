#Created by: Nikhil Polpakkara
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

path = 'M:\Git repository\Python\Exercise files\Basic Data processsing and Visualisation\Final Project\Dataset\games_details.csv'
df_games = pd.read_csv(path)

No_of_games = [d for d in df_games.groupby('GAME_ID',axis=0)]

df = df_games.groupby('GAME_ID',axis=0)


