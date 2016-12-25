#! /usr/local/bin/python3

import requests
from bs4 import BeautifulSoup

base_url = "http://onelinefun.com"
selector = ".oneliner p"
nextpage = ""

outfile = "jokes.txt"

w = open(outfile, 'w',)

jokes = []
for x in range(1,50):
    url = base_url + "/{}/".format(x)
    print(url)
    a = requests.get(url)
    b = a.content.decode('ISO-8859-1')
    print(a)
    c = BeautifulSoup(b, 'html.parser')
    d = c.select(selector)
    for e in d:
        try:
            x  = e.text.rstrip()
            if len(x) > 2:
                w.write(x+'\n')
        except Exception as e:
            print(e)
            pass

w.close()
