#! /usr/bin/python3
# linkverification.py
# mauduong
# 28/03/2019

import sys, requests
from bs4 import BeautifulSoup

def getLink(url):
    print('Starting...')
    req = requests.get(url)
    req.raise_for_status()
    html_content = req.text
    soup = BeautifulSoup(html_content, "html.parser")
    print('Getting URLs...')
    for i in soup.find_all('a'):
        req.requests.get(i)
        if (req.status_code == 404):
            print('URL: ' + req.text + ' 404 Page Not Found Error.')
    print('Done.')

url = sys.argv[1]
getLink(url) 