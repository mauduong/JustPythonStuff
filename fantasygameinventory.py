# Fantasy Game Inventory using Dictionaries
characterItemPouch = {'Dragonslayer Greatbow':1, 'Arrows':10, 'Zweihander':1, 'Throwing Knives':20, 'Binoculars':1, 'Souls':5032}

def displayInventory(inv):
    print("Inventory:")
    item_total = 0
    for k,v in inv.items():
        print(str(v) + ' ' + (k))
        item_total += v
    print("Total number of items: " + str(item_total))
    
displayInventory(characterItemPouch)