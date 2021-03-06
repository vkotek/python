# -*- coding: utf-8 -*-
"""
Created on Fri Dec 26 23:51:57 2014

@author: vkotek
"""

import csv
import math
import collections
from itertools import permutations

words_original = "words_original.txt"
words_filtered = "words_filtered.txt"
words_values = "words_values.csv"

dictionary = [line.split('\n') for line in open(words_filtered, 'r').readlines()]

words_values_dict = {}

# Filters word file for files >16 chars.
def filter_words():
    f = open(words_original, 'r')
    w = open(words_filtered, 'w')
    x = 0
    z = 0
    for line in f:
        if len(line) < 16:
            w.write(line)
            x += 1
        else:
            print(line)
            z += 1
    print(x, "copied")
    print(z, "ommitted")
    f.close()

def checkword(word):
    f = open(words_filtered, 'r')
    if word in f.read():
        return True
    else:
        return False
    f.close()
            
def import_values():
	val = open(words_values)
	csv_val = csv.reader(val)
	for row in csv_val:
		words_values_dict[row[0]] = row[1]

def checkvalue(word):
    import_values()
    x = 0
    word_val = 0
    while x < len(word):
        word_val+=int(words_values_dict[word[x]])
        x+=1
    return word_val

def checkend(word):
    endlist = []
    f = open(words_original, 'r')
    for line in f:
        sline = line.rstrip()               # .rstrip gets rid off \n
        if word == sline[-len(word):]:
            endlist.append(sline)
    if len(endlist) > 0:
        endlist.sort(key = len)
        return endlist
    else: 
        return None

def checkstart(word):
    startlist = []
    f = open(words_filtered, 'r')
    for line in f:              
        if word == line[:len(word)]:
            startlist.append(line.rstrip()) 
    if len(startlist) > 0:
        startlist.sort(key = len)
        return startlist
    else: 
        return None

def permutate(word):
    print("<<< SEARCHING WORDS >>>")
    wordlist = {}
    for a in range(2,len(word)+1):
        awords = []
        wordlist[a] = [''.join(i) for i in permutations(word,a)]
        print("Searching", a,"letter words.")
        for x in wordlist[a]:
            for y in dictionary:
                if x not in awords and x == y[0]:
                    awords.append(x)
                    print(x)
            else:
                pass
    return "<<< END OF SEARCH >>>"

def count_permute(word): # first finds duplicates for denominator
    d = collections.defaultdict(int) 
    denominator = 1
    for c in word:
        d[c] += 1
    for c in sorted(d, key=d.get, reverse=True):
        if d[c] > 1:
            denominator = denominator * (math.factorial(d[c]))
    factlist = [len(word)]
    for x in range(len(word)-1,0,-1):
        factlist.append(factlist[-1]*x)
    return int(int(math.fsum(factlist))/denominator)
    
def overview(word):
    try:
        start = len(checkstart(word))
    except:
        start = None
    try:
        end = len(checkend(word))
    except:
        end = None
    return """
    Word:\t%s\t\tCombs:\t\t%s
    Exists:\t%s\t\t\tBegin w/:\t%s 
    Points:\t%s\t\t\tEnd w/:\t\t%s
    """ % (
        word.capitalize().ljust(15),
        count_permute(word),
        checkword(word),
        start,
        checkvalue(word),
        end
        )
    
while True:
    print("-"*70)
    word_raw = input("Enter Word or Letters: ")
    word = word_raw.lower()
    print(overview(word))
    runit = str(input("\t[1] Check dictionary & points\n\t[2] Words beginnig with..\n\t[3] Words ending with..\n\t[4] Find combinations\n\t[5] Enter new word\n\n..."))
    if runit == '1':
        if checkword(word) is True:
            print("\t",word.capitalize(), "is in the dictionary")
    elif runit == '2':
        print(checkstart(word))
    elif runit == '3':
        print(checkend(word))
    elif runit == '4':
        print(permutate(word))
    elif runit == '5':
        continue
    elif runit == '6':
        print("Filtering words..")
        filter_words()
    else:
        print("Not a valid choice")
