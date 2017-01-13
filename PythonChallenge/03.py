#! /usr/local/bin/python3
# Python Challenge 3

fl = "/Users/ares/Documents/Scripts/python/challenge/03.txt"

t = open(fl, 'r').read().replace('\n','')

out = ""

# non regex function - missing small letters at each side.
for x in range(3, len(t)-3):
    a = t[x-3:x]
    b = t[x]
    c = t[x+1:x+4]
    if a.isupper() and b.islower() and c.isupper():
        #print(t[x-3:x+4])
        out += t[x]

print(out) # is nonsense..


# regex attempt
import re

reg = "([a-z][A-Z]{3})([a-z])([A-Z]{3}[a-z])"
m = re.findall(reg, t)
result = [x[1] for x in m ]
print("".join(result)) # Result

# XXX in all directions (up and down too) incomplete
