# Fantasy Game Inventory using Dictionaries
import random

characterItemPouch = {'Dragonslayer Greatbow':1, 'Arrows':10, 'Zweihander':1, 'Throwing Knives':20, 'Binoculars':1, 'Souls':5032}
yhormTheGiantDrops = ['Souls', 'Soul of Yhorm the GIant', 'Cinders of a Lord']

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k,v in inventory.items():
        print(str(v) + ' ' + (k))
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(characterItemPouch)

def addToInventory(inventory, addedLoot):
    for item in addedLoot:
        inventory.setdefault(item, 0)
        if item == 'Souls':
            inventory[item] += 3600
        else:
            inventory[item] += 1
    return inventory

inv = {'Souls': 1000, 'Zweihander': 1} 
inv = addToInventory(characterItemPouch, yhormTheGiantDrops)    
displayInventory(inv)
