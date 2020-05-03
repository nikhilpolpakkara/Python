import random

def problem2_6():
    random.seed(431)
    for j in range (0,100):
        dice2 = random.randint(1,6)
        dice1 = random.randint(1,6)
        j = j+1
        print(dice1+dice2)
        