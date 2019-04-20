#! /usr/bin/python3
# downloadWithRequest.py
# mauduong
# 24/03/2019

import requests

req = requests.get('http://textfiles.com/100/apples.txt')
req.raise_for_status()
playFile = open('fileOutput.txt', 'wb') # Write in Binary

for chunk in req.iter_content(100000):
    playFile.write(chunk)

playFile.close()
