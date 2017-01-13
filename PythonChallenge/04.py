#! /usr/local/bin/python3
# Python Challenge 4

import requests as r

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
x = 0

def getNext(n):

    global x

    a = r.get(url, {'nothing': n})
    x += 1

    # print("{}\t{}".format(x, a.text))

    b = a.text.split()

    try:
        c = int(b[-1])
        getNext(c)
    except:
        print(a.text)
        getNext(input("nothing="))

end = getNext(27709)
