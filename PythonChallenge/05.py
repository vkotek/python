#! /usr/local/bin/python3
# Python Challenge 5

import pickle

fl = "/Users/ares/Documents/Scripts/python/challenge/05.p"

with open(fl, 'rb') as f:
    data = pickle.load(f)

for row in data:
    for item in row:
        print(item[0]*item[1], end="")
    print('')
