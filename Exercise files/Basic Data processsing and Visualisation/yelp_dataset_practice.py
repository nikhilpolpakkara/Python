#Created by: Nikhil Polpakkara
#Created by: Nikhil Polpakkara
import json
import ast
from collections import defaultdict
from datetime import datetime

path = "M:/Dataset/yelp_dataset.json"
f = open(path,'r', encoding='utf-8')

#cnt = 0 
#for line in f:
    

dataset = []

for i in range(100):
    try:
        dataset.append(json.loads(f.readline()))
    except:
        continue

#%%
#how to make a dictionary with list
funny_name = defaultdict(list)

for d in dataset:
    funny_name[d['name']].append(d['funny'])
#%%  
#most longest yelping user
for d in dataset:
    a = d['yelping_since'].split()
    t = datetime.fromisoformat(a[0]).timestamp()
    current_date = datetime.fromisoformat('2020-05-10').timestamp()
    diff = current_date - t
#%%
def count_num_friends(friends_list):
    friends = list(friends_list.split())
    num_friends = len(friends)
    return num_friends

friend_count = {}
for d in dataset:
    friends = d['friends']
    friend_count[d['name']] = count_num_friends(friends)

friends_count = [(friend_count[p],p) for p in friend_count]
friends_count.sort()
Top_friends = friends_count[-10:]
