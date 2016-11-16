import os
from move import *
import random
import time
from termcolor import cprint


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
        game_board[y+4][x+5+7] = 'O'  # tavern man
    if level == 2:
        x = random_area[1]
        y = random_area[0]
        for i in range(y+4, y+8):
            for z in range(x+4, x+19):
                if i == y+4 or i == y+7 or z == x+4 or z == x+18:
                    game_board[i][z] = '#'
        game_board[y+7-1][x+4] = '.'
        game_board[y+5][x+10+7] = 'B'  # farmer wife
        while x == random_area[1] and y == random_area[0]:  # random area for wheat
            x = random.randrange(0, 31, 30)
            y = random.randrange(0, 11, 10)
        for i in range(y+2, y+8):  # wheat  generating
            for z in range(x+3, x+27):
                    game_board[i][z] = chr(182)#'/'

    if level == 3:
        x = random_area[1]
        y = random_area[0]
        for i in range(y+3, y+8):
            for z in range(x+9, x+17):
                if i == y+3 or i == y+7 or z == x+9 or z == x+16:
                    game_board[i][z] = '#'
        game_board[y+7][x+5+7] = '.'
        game_board[y+7][x+6+7] = '.'
        game_board[y+4][x+5+7] = chr(216) # boss
        while x == random_area[1] and y == random_area[0]:  # random area for new build
            x = random.randrange(0, 31, 30)
            y = random.randrange(0, 11, 10)
        for i in range(y+2, y+7):
            for z in range(x+8, x+18):
                if i == y+2 or i == y+6 or z == x+8 or z == x+17:
                    game_board[i][z] = '#'
        game_board[y+3][x+8] = '.'
    return game_board


def intro(level):
    os.system('clear')
    print("\nLEVEL ",level)
    if level == 1:
        print("""
        You are a drunkard farmer. Last night
        you drank too much. You don't know what is going on.
        Talk to host if you want know what is your name.
        Good luck!
        """)
    elif level == 2:
        print("""
        After you get all your clothes you go to your farm.
        From a distance you hear the voice of your wife.
        You have bad feelings...
        """)
    elif level == 3:
        print("""
        It's time to sell your harvest. You go to city
        and you see two buildings, in one of them is shopkeeper.
        Talk to him.
        """)
    input("Click anything to continue")


def levels(level):
    inventory = 0
    if level == 1:
        intro(level)
        player_x = 3
        player_y = 3
        game_board = board(20, 60, player_x, player_y)
        game_board = random_buildings(game_board, level)
        game_board = random_item(game_board)
    if level == 2:
        intro(level)
        player_x = 1
        player_y = 1
        game_board = board(20, 60, player_x, player_y)
        game_board = random_buildings(game_board, level)
    if level == 3:
        intro(level)
        player_x = 3
        player_y = 3
        game_board = board(20, 60, player_x, player_y)
        game_board = random_buildings(game_board, level)
        game_board = random_item(game_board)

    while True:
        os.system('clear')
        show_board(game_board)
        move_variables = movement(game_board, player_x, player_y, inventory)
        game_board = move_variables[0]
        player_x = move_variables[1]
        player_y = move_variables[2]
        inventory = move_variables[3]


def fun_effectwow():
    """Special effect"""
    f = open("effect.txt", 'r')
    colorlist = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    effect_list = [line[:-1] for line in f]
    f.close()
    maxlen = len(effect_list[0])
    for i in range(round(maxlen/2)+2):
        os.system('clear')
        for z in range(len(effect_list)):
            cprint(effect_list[z][:i] + (" " * (maxlen-i*2)) + effect_list[z][maxlen-i:], random.choice(colorlist))
        time.sleep(0.05)


def main():
    while True:
        os.system('clear')
        fun_effectwow()
        print("\n▁▂▄▅▆▇█ FARMER GAME █▇▆▅▄▂▁\n\n1. PLAY\n2. HELP\n3. QUIT\n")
        user_choice = input("You pick: ")
        if user_choice == "1":
            levels(1)
            levels(2)
            levels(3)
        elif user_choice == "2":
            print("May the force be with you")
            input()
        elif user_choice == "3":
            quit()
        else:
            print("Wrong command")
            input()


if __name__ == "__main__":
    main()
