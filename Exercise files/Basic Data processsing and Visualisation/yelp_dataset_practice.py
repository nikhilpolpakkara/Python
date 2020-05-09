#Created by: Nikhil Polpakkara
#Created by: Nikhil Polpakkara
import json
import ast
path = "M:/Dataset/yelp_dataset.json"
f = open(path,'r', encoding='utf-8')


dataset = []
for i in range(50):
    dataset.append(json.loads(f.readline()))

dataset[0]
