#! usr/local/bin/python3
# singleOccurrence.py
# mauduong
# 07/10/2019
# Find an element that occurs once where other elements occur three times

def singleOccurrence(length, array):
    one = 0 # XOR element that appears once
    two = 0 # XOR element that appears twice

    for i in range(length):
        two = two | (one & array[i]) # bitwise OR 
        one = one ^ array[i]         # bitwise XOR
        bit_mask = ~(one & two)      # invert AND  same as import operator .. operator.invert(one & two)
        one &= bit_mask              # same functionality as import operator .. operator.__iand__(one, bit_mask)
        two &= bit_mask              # equivalent to two &= bit_mask
    return one

array = [10, 10, 10, 20, 30, 30, 30, 40, 40, 40, 20, 50, 20]
length = len(array)

print("Single occurance: ", singleOccurrence(length, array))

