import string


# inv must be empty before import

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
    for item in loot:
        if item[0] in inventory.keys():
            inventory[item[0]][0] += 1  # amount
            inventory[item[0]][2] += item[2]  # weight
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
    sorted_dict = sorted(inventory.items(), key=lambda index: index[1], reverse=True)  # sort by amount
    print('Inventory:')
    print('{:>12} {:>7} {:>7}'.format('item name', 'amount', 'weight'))
    print('-' * max_len)
    for key, value in sorted_dict:
        print('{:>12} {:>7} {:>7}'.format(key, value[0], value[2]))
    print('-' * max_len)
    print('Total number of items: {}'.format(sum(amount)))
    print('Total weight: {}'.format(sum(weight)))


def fastsplit(line):
    """Split line from imported file"""
    line = [l.strip().split(',') for l in line]  # strip() remove \n and stuff like this
    return line


def import_inventory(inventory, filename):
    """Importing inventory from file and merging with current inventory"""
    file_loot = open(filename, 'r')
    loot = fastsplit(file_loot)
    for item in loot:
        inventory[item[0]] = [int(item[1]), item[2], int(item[3])]
    print(loot)
    return inventory


def export_inventory(inventory, filename='export_inventory.csv'):
    """export data to file"""
    export_file = open(filename, 'w+')
    for key, value in inventory.items():
            export_file.write('{},{},{},{}\n'.format(key, value[0],value[1],value[2]))

# create bag of secret items in def to call from module
def random_items():
    pass

def main():
    """check all def"""
    #inv = {'rope': [1, 'other', 12], 'torch': [6, 'other', 12], 'gold coin': [42, 'other', 42],
          # 'dagger': [1, 'weapon', 2],
           #'arrow': [12, 'weapon', 12]}
    loot = [['gold coin', 'other', 1], ['dagger', 'weapon', 2], ['gold coin', 'other', 1], ['gold coin', 'other', 1],
            ['ruby', 'other', 1]]
    inv = {}
    print(inv)
    import_inventory(inv,'export_inventory.csv')
    print_table(inv)
    display_inventory(inv)
    export_inventory(inv)


if __name__ == '__main__':
    main()
