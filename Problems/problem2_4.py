import random

def problem2_4():
    random.seed(70)
    list_ = []
    for i in range (0,10):
        list_.append(random.random())
        list_[i]=list_[i]*5 + 30
        i= i+1
    print(list_)