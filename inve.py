def display_inventory(inventory):
    """prints keys and values of inventory"""
    weight = []
    amount = []
    print('Inventory:')
    for key, value in inventory.items():
        print('{} {}'.format(value[0], key))
    for value in inventory.values():
        weight.append(value[2])
        amount.append(value[0])
    print('total weigh of items: {}'.format(sum(weight)))
    print('Total number of items: {}'.format(sum(amount)))


def add_to_inventory(inventory, loot):
    """ adding items from lists to inventory"""
    #inv = {'rope': [1, 'other', 12], 'torch': [6, 'other', 12], 'gold coin': [42, 'other', 42],
    #       'dagger': [1, 'weapon', 2],
    #       'arrow': [12, 'weapon', 12]}
    #loot = [['gold coin', 'other', 1], ['dagger', 'weapon', 2], ['gold coin', 'other', 1], ['gold coin', 'other', 1],
    #        ['ruby', 'other', 1]]
    for item in loot:
        if item[0] in inventory.keys():
            inventory[item[0]][0] += 1 # amount
            inventory[item[0]][2] += item[2] # weight
        else:
            inventory[item[0]] = [1, item[1], item[2]]
    return inventory


def print_table(inventory):
    """print backpack in order"""
    amount = []
    weight = []
    for value in inventory.values():
        amount.append(value[0])
        weight.append(value[2])
    list_of_len = [len('{:>12} {:>7} {:>7}'.format(key, value[0], value[2])) for key, value in inventory.items()]
    max_len = max(list_of_len)
    sorted_dict = sorted(inventory.items(), key=lambda index: index[1], reverse=True)  # sort by value
    print('Inventory:')
    print('{:>12} {:>7} {:>7}'.format('item name', 'amount', 'weight'))
    print('-' * max_len)
    for key, value in sorted_dict:
        print('{:>12} {:>7} {:>7}'.format(key, value[0], value[2]))
    print('-' * max_len)
    print('Total number of items: {}'.format(sum(amount)))
    print('Total weight: {}'.format(sum(weight)))


def import_inventory(inventory, filename='import_inventory.csv'):
    """import data from file"""
    import_file = open(filename, 'r')
    file = [list(line) for line in import_file]
    for item in file:
        for x in item:
            if x == ',':
                item_file = ''.join(item[:item.index(x)])  # its value
                if item[-1] == '\n':
                    if item_file in inventory.keys():
                        inventory[item_file] += float(''.join(item[item.index(x) + 1:-1]))
                    else:
                        try:
                            float(''.join(item[item.index(x) + 1:-1]))
                            inventory[item_file] = float(''.join(item[item.index(x) + 1:-1]))
                        except ValueError:
                            pass
                else:
                    if item_file in inventory.keys():
                        inventory[item_file] += float(''.join(item[item.index(x) + 1:]))
                    else:
                        try:
                            float(''.join(item[item.index(x) + 1:]))
                            inventory[item_file] = float(''.join(item[item.index(x) + 1:]))
                        except ValueError:
                            pass


def export_inventory(inventory, filename='export_inventory.csv'):
    """export data to file"""
    if filename is 'export_inventory.csv':
        export_file = open('export_inventory.csv', 'w+')
        for key, value in inventory:
            export_file.write('{},{}'.format(key, value))
    else:
        export_file = open(filename, 'w+')
        for key, value in inventory.items():
            export_file.write('{},{}\n'.format(key, value))


def main():
    """check all def"""
    inv = {'rope': [1, 'other', 12], 'torch': [6,'other',12], 'gold coin': [42, 'other', 42], 'dagger': [1,'weapon', 2],
           'arrow': [12, 'weapon', 12]}
    loot = [['gold coin', 'other', 1], ['dagger', 'weapon', 2], ['gold coin', 'other', 1], ['gold coin', 'other', 1], ['ruby', 'other', 1]]
    display_inventory(inv)
    add_to_inventory(inv, loot)
    display_inventory(inv)
    print(inv)
    print_table(inv)
    import_inventory(inv)
if __name__ == '__main__':
    main()