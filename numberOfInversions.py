#! usr/local/bin/python3
# numberOfInversions.py
# mauduong
# 13/10/2019
# Count the number of inversions in a given array

def getInversions(array, num):
    inversion = 0;
    
    for i in range(num):
        for j in range(i + 1, num):
            if (array[i] > array[j]):
                inversion += 1
    
    return inversion

array = [1,2,3,4,5,4,3,1,8,4,9,1]
num = len(array)
print("Number of inversions: ", getInversions(array, num))