#! usr/local/bin/python3
# rand5rand7.py
# mauduong
# 13/10/2019
# Generate a random number within the range of 1 to inclusive 5, and within the range of 1 to inclusive 7.

import random

def rand5():
    return random.randrange(1,6)

def rand7():
    return random.randrange(1,8)

print("rand5 function output: ", rand5())
print("rand7 function output: ", rand7())