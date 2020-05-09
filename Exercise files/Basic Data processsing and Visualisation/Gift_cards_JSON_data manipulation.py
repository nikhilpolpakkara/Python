#Created by: Nikhil Polpakkara
import json
import ast
import numpy as np
from collections import defaultdict

path = "M:/Git repository/Python/JSON/Gift_Cards.json"
f = open(path,'r',encoding='utf-8')
j = json.loads(f.readline())
k = []
k.append(f.readline())


list =[]
for line in f:
    fields = line.strip().split('\t')
    list.append(fields)

#for i in range(0,len(list)):

d=json.loads(k[0])

cnt = 0
for i in f:
    cnt = cnt +1
print(cnt)

lst = []
for i in range(0,1000):
    lst.append(f.readline())
nl = []
for i in range(0,len(lst)):
    m = json.loads(lst[i])
    nl.append(m)
    
#%%
dataset = []
for i in range(1000):
    dataset.append(json.loads(f.readline()))

#%%
#Calculating mean from the data
sum_ = 0    
for i in range(1000):
    a = dataset[i]['overall']
    sum_ = sum_ + a
mean = sum_/len(dataset)
print(mean)

for i in range(1000):
    mean = np.mean(dataset[i]['overall'])
#%%
#making a list of overall ratings
di = []
for d in dataset:
    a = d.get('overall')
    di.append(a)

#%%
# dictionary of overall ratings
rate_count = {1:0,2:0,3:0,4:0,5:0}
for i in range(1000):
    rate_count[dataset[i]['overall']] += 1
rate_count
#%%
#Counting verified purchases
verifiedcounts = defaultdict(int)
for d in dataset:
    verifiedcounts[d['verified']] += 1
#%%
#popular product id
Prod_popular = defaultdict(int)
for d in dataset:
    Prod_popular[d['asin']] += 1
sort_list = [(Prod_popular[p],p) for p in Prod_popular]
sort_list = sorted(sort_list, key=lambda x: x[0], reverse=True)
