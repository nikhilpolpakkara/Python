#Created by: Nikhil Polpakkara
import json
import ast
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