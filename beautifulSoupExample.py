#! /usr/bin/python3
# beautifulSoupExample.py
# mauduong
# 24/03/2019

import requests, bs4

req = requests.get('http://hmm.com')
req.raise_for_status()
soup = bs4.BeautifulSoup(req.text)
print(type(soup))

# Opening a file locally
localFile = open('henlo.html')
localSoup = bs4.BeautifulSoup(localFile.read())
element = localSoup.select('#element')
print(type(element))
print(len(element))
print(type(element[0]))
element[0].getText()
str(element[0])
element[0].attrs
element.get('id')
element = localSoup.select('span')[0]

