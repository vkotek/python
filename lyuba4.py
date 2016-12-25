#! /usr/local/bin/python3

import requests
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser
import codecs

outfile = "/Users/ares/Desktop/victory_1book.txt"

with open(outfile, 'w') as f:
    f.write("")

with codecs.open("/Users/ares/Desktop/urllist1.txt",'r','utf-8') as m:
    for url in m:
        new_url = url.strip()
        print(url)
        pr_text = requests.get(new_url)
        print(pr_text.text)
        victory_soup = BeautifulSoup(pr_text, "html.parser")
        print(victory_soup)
        try:
            zag = victory_soup.find("h1").text.strip()
            programm = victory_soup.find("div", class_="dialog").text.strip()


            with codecs.open(outfile, "a", 'utf-8') as victory:
                victory.write(zag)
                victory.write(programm)
            print("OK"+'\t'+zag)
        except Exception as e:
            print("ERROR"+'\t'+url)
