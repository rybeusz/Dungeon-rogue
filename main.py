import os
from move import *


def board(x, y, player_x, player_y):
    """Create a board"""
    list = []
    for row in range(x):
        list.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                list[row].append('#')
            else:
                list[row].append('.')
    list[player_x][player_y] = '@'
    return list


def show_board(list):
    for i in list:
        print(''.join(i))

def main():
    player_x = 3
    player_y = 3
    game_board = board(15, 50, player_x, player_y)

    while True:
        os.system('clear')
        show_board(game_board)
        zwrot = movement(game_board, player_x, player_y)
        game_board = zwrot[0]
        player_x = zwrot[1]
        player_y = zwrot[2]


if __name__ == "__main__":
    main()
