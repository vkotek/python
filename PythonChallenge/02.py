#! /usr/local/bin/python3
# Python Challenge 2

fl = "/Users/ares/Documents/Scripts/python/challenge/02.txt"

alphabet = 'abcdefghijklmnopqrstuvwxyz'

out = ''

with open(fl, 'r') as f:
    for char in f.read():
        if char in alphabet:
            out+=char

print(out)
