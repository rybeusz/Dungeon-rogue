def display_inventory(inventory):
    """prints keys and values of inventory"""
    weight = []
    print('Inventory:')
    for key, value in inventory.items():
        print('{} {}'.format(value[0], key))
    for value in inventory.values():
        weight.append(value[0])

    print('Total number of items: {}'.format(sum(weight)))


def add_to_inventory(inventory, loot):
    """ adding items from lists to inventory"""
    #loot = [['gold coin', 'other'], ['dagger', 'weapon'], ['gold coin', 'other'], ['gold coin', 'other'], ['ruby', 'other']]
    #inv = {'rope': [1, 'other'], 'torch': [6,'other'], 'gold coin': [42, 'other'], 'dagger': [1,'weapon'],
    #       'arrow': [12, 'weapon']}
    #backpack[items[0][0]].append(items[0][1])
    for item in loot:
        if item[0] in inventory.keys():
            inventory[item[0]][0] += 1
        else:
            inventory[item[0]] = [1, item[1]]
    return inventory


def print_table(inventory, order=None):
    """print inventory in order or no"""
    list_of_len = [len('{:>6} {:>12}'.format(value, key)) for key, value in inventory.items()]
    max_len = max(list_of_len)
    elif order == 'count,desc':
        sorted_dict = sorted(inventory.items(), key=lambda index: index[1], reverse=True)  # sort by value
        print('Inventory:')
        print("{:>6} {:>12}".format('count', 'item name'))
        print('-' * max_len)
        for key, value in sorted_dict:
            print('{:>6} {:>12}'.format(value, key))
        print('-' * max_len)
        print('Total number of items: {}'.format(sum(inventory.values())))
    elif order == 'count,asc':
        sorted_dict = sorted(inventory.items(), key=lambda index: index[1], reverse=False)
        print('Inventory:')
        print("{:>6} {:>12}".format('count', 'item name'))
        print('-' * max_len)
        for key, value in sorted_dict:
            print('{:>6} {:>12}'.format(value, key))
        print('-' * max_len)
        print('Total number of items: {}'.format(sum(inventory.values())))


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
    inv = {'rope': [1, 'other'], 'torch': [6,'other'], 'gold coin': [42, 'other'], 'dagger': [1,'weapon'],
           'arrow': [12, 'weapon']}
    loot = [['gold coin', 'other'], ['dagger', 'weapon'], ['gold coin', 'other'], ['gold coin', 'other'], ['ruby', 'other']]
    display_inventory(inv)
    add_to_inventory(inv, loot)
    display_inventory(inv)
    print(inv)
if __name__ == '__main__':
    main()