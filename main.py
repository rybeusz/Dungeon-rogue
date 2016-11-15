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


def random_buildings(game_board, level):
    random_area = [random.randrange(0, 11, 10), random.randrange(0, 31, 30)]
    if level == 1:
        x = random_area[1]
        y = random_area[0]
        for i in range(y+3, y+8):
            for z in range(x+7, x+19):
                if i == y+3 or i == y+7 or z == x+7 or z == x+18:
                    game_board[i][z] = '#'
        game_board[y+7][x+5+7] = '.'  # tavern doors
        game_board[y+7][x+6+7] = '.'  # tavern doors
    if level == 2:
        x = random_area[1]
        y = random_area[0]
        for i in range(y+4, y+8):
            for z in range(x+4, x+19):
                if i == y+4 or i == y+7 or z == x+4 or z == x+18:
                    game_board[i][z] = '#'
        game_board[y+7-1][x+4] = '.'

        while x == random_area[1] and y == random_area[0]: # random area for wheat
            x = random.randrange(0, 31, 30)
            y = random.randrange(0, 11, 10)

        for i in range(y+2, y+8):
            for z in range(x+3, x+27):
                    game_board[i][z] = '/'


    if level == 3:
        pass
    return game_board


def levels(level):
    inventory = 0
    # level 1
    if level == 1:
        player_x = 3
        player_y = 3
        game_board = board(20, 60, player_x, player_y)
        game_board = random_item(game_board)
        game_board = random_buildings(game_board, level)
    # level 2
    if level == 2:
        player_x = 1
        player_y = 1
        game_board = board(20, 60, player_x, player_y)
        #game_board = random_item(game_board)
        game_board = random_buildings(game_board, level)
    # level 3
    if level == 3:
        pass

    while True:
        os.system('clear')
        show_board(game_board)
        move_variables = movement(game_board, player_x, player_y, inventory)
        game_board = move_variables[0]
        player_x = move_variables[1]
        player_y = move_variables[2]
        inventory = move_variables[3]


def main():
    #levels(1)
    levels(2)
    levels(3)


if __name__ == "__main__":
    main()
