backpack = {'clothes':[['coat', 2.3],['hat', 3]], 'food': [], 'weapons': [['mace', 3, 2]], 'other': []}

items = [['clothes', ['coat', 2.3], ['hat', 3], ['scarf', 1]], ['food',['meat', 1], ['humus', 0.5]], ['weapons',
        [['spoon', 1, 4], ['mace', 3, 2]], ['other',['rifle', 5], ['ammo', 0.1]]]]

backpack[items[0][0]].append(items[0][1])
weight = []
strght = []
item_to_remove = ['coat']
print(backpack)

for value in backpack.values():
    for we in value:
        try:
            weight.append(we[1])
        except IndexError:
            pass

for value in backpack.values():
    for we in value:
        if we[0] in item_to_remove:
            value.remove(we)
            break

for value in backpack['weapons']:
    strght.append(value[2])

print(backpack)
print(int(sum(weight)))
print(int(sum(strght)))