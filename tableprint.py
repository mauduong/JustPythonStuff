# tableprint.py
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

table = {0:[], 1:[], 2:[], 3:[]}

for i in tableData:
    for j in range(len(i)):
        table[j].append(i[j])

longest = 0

for k, v in table.items():
    length = len(''.join(v))
    if length > longest:
        longest = length

for k, v in table.items():
    print('' * (longest - len(''.join(v))) + ' '.join(v))