#Created by: Nikhil Polpakkara
import json
import ast
import numpy as np
from collections import defaultdict

path = "M:/Git repository/Python/JSON/Gift_Cards.json"
f = open(path,'r',encoding='utf-8')

dataset = []
while len(dataset) <1000:
    dataset.append(json.loads(f.readline()))

overall = [d['overall'] for d in dataset]
review_time = [d['reviewTime'] for d in dataset]
reviewer_name = [d['reviewerName'] for d in dataset]

overall = np.array(overall)
review_time = np.array(review_time)
reviewer_name = np.array(reviewer_name)
np.mean(overall)
np.stack([overall,review_time,reviewer_name]).T


import numpy
numpy.eye(3)