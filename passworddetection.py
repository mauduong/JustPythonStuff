# passworddetection.py

import re

pw = raw_input("Enter a password: ")

eightCharacters = re.compile(r'.{8,}')
characterMatch = eightCharacters.search(pw)

capitalCharacter = re.compile(r'?=.*?[A-Z]')
upperMatch = capitalCharacter.search(pw)

lowerCaseCharacter = re.compile(r'?=.*?[a-z]')
lowerMatch = lowerCaseCharacter.search(pw)

oneDigit = re.compile(r'?=.*?[0-9]')
digitMatch = oneDigit.search(pw)


specialCharacter = re.compile(r'?=.*?[!@#$%^&*-]')
specialMatch = specialCharacter.search(pw)

if characterMatch == None:
    print('Please enter at least eight characters.')
if upperMatch == None:
    print('Please enter at least an Uppercase character.')
if lowerMatch == None:
    print('Please enter at least a Lowercase character.')
if digitMatch == None:
    print('Please enter at least one number.')
if specialMatch == None:
    print('Please enter at least one special character.')