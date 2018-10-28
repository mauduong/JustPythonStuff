import sys

def collatz(number):
    if (number % 2 == 0):
        return (number // 2)
    elif (number % 2 == 1):
        return (3 * number + 1)

while True:
    print('Enter a number: ')
    try:
        number = input()
        getCollatzNumber = collatz(int(number))
    
        print('Input number: ' + str(number) + '\tCollatz number: ' + str(getCollatzNumber))
        print('')
        if (getCollatzNumber == 1):
            break
    except:
        print('You need to enter an integer value.')
        print('')
        