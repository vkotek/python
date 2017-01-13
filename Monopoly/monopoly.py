#! /usr/local/bin/python3
# https://github.com/jm-contreras/monopoly/blob/master/monopoly.ipynb
# Dice simulation

import random
from collections import Counter

def diceThrow():

    a = random.randrange(1,7,1)
    b = random.randrange(1,7,1)

    if a == b:
        double = True
    else:
        double = False

    return { 'a': a, 'b': b,'sum': a + b, 'double': double }


def board():
    # Define fields
    fields = [ x for x in range(0,40)]

def throwStats(n):
    throw = []
    for i in range(n):
        print(diceThrow())


class game(object):

    def __init__(self, players):
        players = {}
        #for player in range(players):

    def player(self):
        self.position = 0
        

fields = [ x for x in range(0,40)]

for x in fields:
    print("{}\t{}".format(x,x*x))

if __name__ == '__main__':
    throwStats(60)
