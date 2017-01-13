#! /usr/local/bin/python3
# -*- coding: utf-8 -*-

url = "http://echo.msk.ru/programs/victory/"
url = "http://echo.msk.ru/programs/zdor/"
base_url = "http://echo.msk.ru"
outfile = "echo.txt"

import requests
from bs4 import BeautifulSoup
class echoParser(object):

    def __init__(self,url,outfile):
        self.success = 0
        self.failed = 0
        self.links = []
        self.pages = 0
        self.writer(url,outfile)

    def getNextPage(self, page):
        try:
            next_url = page.select('.pager a.next')[0].get('href')
            self.pages += 1
            return base_url + next_url
        except:
            return False

    def getArticlesUrl(self, url):
        # Get all article urls from current page
        page = BeautifulSoup( requests.get(url).text , 'html.parser')
        for link in page.select('#archive .prevcontent .meta .view'):
            self.links.append(base_url+link.get('href'))
        if self.getNextPage(page) != False:
            self.getArticlesUrl(self.getNextPage(page))
        return self.links

    def getArticleContent(self, url):
        # Get the content of an article
        article = BeautifulSoup( requests.get(url).text , 'html.parser')
        body = []
        try:
            text = article.find('div','mmplayer')
            for p in text.find_all('p'):
                x = p.text
                body.append(x.encode('utf-8'))
            body = b'\n'.join(body)
            self.success += 1
            return body
        except Exception as e:
            self.failed += 1
            # return empty byte string
            return b''

    def writer(self, url, outfile):
        with open(outfile,'wb') as f:
            for link in self.getArticlesUrl(url):
                text = self.getArticleContent(link)
                f.write(text)
        print("{0}/{1} articles on {2} pages saved to '{3}'".format( self.success, self.failed, self.pages, outfile ))


x = echoParser(url, outfile)
