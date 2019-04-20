#! /usr/bin/python3
# imageDownloader.py
# mauduong
# 27/03/2019

import sys, bs4, re, os, requests

def imageDownloader(url, category):
    os.makedirs(category + ' folder', exist_ok=True)

    req = requests.get(url + '/search?q=' + category)
    req.raise_for_status()
    soup = bs4.BeautifulSSoup(req.text, "html.parser")

    regex = re.compile(r'(.*?)b(.jpg)$')
    images = soup.select('#imagelist img')

    for i in images:
        if (i.get('alt') == ""):
            source = i.get('src')
            valid = regex.search(source)

            if valid != None:
                src = valid.group(1) + valid.group(2)
                src = 'https:' + src

                imageFile = open(os.path.join(category, os.path.basename(src)), 'wb')
                req = requests.get(src)
                req.raise_for_status()

                for chunk in req.iter_content(100000):
                    imageFile.write(chunk)
                imageFile.close()

url ="https://imgur.com/"
category = sys.argv[1]
imageDownloader(url, category)