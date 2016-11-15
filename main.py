import os
from move import *
import random


def board(x, y, player_x, player_y):
    """Create a board"""
    list = []

    for row in range(x):
        list.append([])
        for column in range(y):
            if row == 0 or row == x - 1 or column == 0 or column == y - 1:
                list[row].append('#')
            else:
                list[row].append('.')
    list[player_x][player_y] = '@'
    return list



def show_board(list):
    for i in list:
        print(''.join(i))


def random_item(list):
    i = 0
    items = ['a', 'b', 'c', 'd', 'e']
    while True:
        x = random.randrange(19)
        y = random.randrange(59)
        if list[x][y] == '.':
            list[x][y] = items[i]
            i += 1
        if i == 5:
            break
    return list


def main():
    player_x = 3
    player_y = 3
    game_board = board(20, 60, player_x, player_y)
    inventory = 0
    game_board = random_item(game_board)
    while True:
        os.system('clear')
        show_board(game_board)
        zwrot = movement(game_board, player_x, player_y, inventory)
        game_board = zwrot[0]
        player_x = zwrot[1]
        player_y = zwrot[2]
        inventory = zwrot[3]


if __name__ == "__main__":
    main()
