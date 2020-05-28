#Created by: Nikhil Polpakkara
import json
import ast
from collections import defaultdict
from datetime import datetime

path = "M:/Git repository/Python/JSON/Gift_Cards.json"
f = open(path,'r',encoding='utf-8')
j = json.loads(f.readline())

review = j['reviewText']
review_wrods = review.split()

k = ' '.join(review_wrods)


lis = ['Try','dry!', 'free/']

import string

def string_processing(string_list):
    lis_ = []
    for x in string_list:
        for char in x:
            if not char in string.punctuation:
                lis_.append(char.lower())
        lis_.append(' ')

    return ''.join(lis_)

    
for x in lis:
    for char in x:
        if not char in string.punctuation:
            lis_.append(char)
    lis_.append(' ')

' '.join(lis_)
