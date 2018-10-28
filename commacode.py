spam = ['apples', 'bananas', 'tofu', 'cats']
spam[-1] = 'and ' + spam[-1]

def listToString(spam):
    string = ', '.join(map(str, spam))
    print(string)

listToString(spam)