#! /usr/local/bin/python3
# Python Challenge 10

a = [1, 11, 21, 1211, 111221]

# len(a[30]) = ?

def getNext(x):
    previous, counter = '', 0
    nxt = ''
    for n in str(x):
        if n != previous and previous != '':
            nxt += '{}{}'.format(counter,previous)
            counter = 0
        counter +=1
        previous = n
    nxt += '{}{}'.format(counter,previous)
    return nxt


while len(a) < 31:
    a.append(getNext(a[len(a)-1]))


print(len(a[30]))
