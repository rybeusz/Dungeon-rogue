import os
from move import *
import random
import time
from termcolor import cprint
import inve


def board(x, y, player_x, player_y):
    """Create a board"""
    game_board = []
    for row in range(x):
        game_board.append([])
        for column in range(y):
            if row == 0 or row == x - 1 or column == 0 or column == y - 1:
                game_board[row].append('█')
            else:
                game_board[row].append('.')
    game_board[player_x][player_y] = '@'
    return game_board


def show_board(game_board):
    """Just show board"""
    for i in game_board:
        print(''.join(i))


def random_item(game_board, items):
    i = 0
    while True:
        x = random.randrange(19)
        y = random.randrange(59)
        if game_board[x][y] == '.':
            game_board[x][y] = items[i]
            i += 1
        if i == len(items):
            break
    return game_board


def generate_build(game_board, x, y, bpY, bpX):
    """Creating buildings"""
    for i in range(y+bpY[0], y+bpY[1]):
        for z in range(x+bpX[0], x+bpX[1]):
            if i == y+bpY[0] or i == y+bpY[1]-1 or z == x+bpX[0] or z == x+bpX[1]-1:
                game_board[i][z] = '█'
    return game_board


def random_buildings(game_board, level):
    """Displaying buildings,corn in random areas"""
    random_area = [random.randrange(0, 11, 10), random.randrange(0, 31, 30)]
    x = random_area[1]
    y = random_area[0]
    if level == 1:
        game_board = generate_build(game_board, x, y, [3, 8], [7, 19])
        game_board[y+7][x+5+7] = '.'  # tavern doors
        game_board[y+7][x+6+7] = '.'  # tavern doors
        game_board[y+4][x+5+7] = 'O'  # tavern man
        game_board = random_item(game_board, ['a', 'b', 'c', 'd', 'e'])  # clothes
    if level == 2:
        game_board = generate_build(game_board, x, y, [3, 8], [4, 19])
        game_board[y+7-1][x+4] = '.'
        game_board[y+5][x+9+7] = '❤'  # farmer wife
        while x == random_area[1] and y == random_area[0]:  # random area for corn
            x = random.randrange(0, 31, 30)
            y = random.randrange(0, 11, 10)
        for i in range(y+2, y+8):  # corn  generating
            for z in range(x+3, x+27):
                    game_board[i][z] = chr(182)
    if level == 3:
        game_board = generate_build(game_board, x, y, [3, 8], [9, 17])
        game_board[y+7][x+5+7] = '.'
        game_board[y+7][x+6+7] = '.'
        game_board[y+4][x+5+7] = "☠"  # boss
        while x == random_area[1] and y == random_area[0]:  # random area for new build
            x = random.randrange(0, 31, 30)
            y = random.randrange(0, 11, 10)
        game_board = generate_build(game_board, x, y, [2, 7], [8, 18])
        game_board[y+3][x+8] = '.'
        game_board[y+5][x+5+7] = '¢'
        game_board = random_item(game_board, ["♏"])
    return game_board


def intro(level):
    """Printing intro before each level"""
    os.system('clear')
    print("\nLEVEL ", level)
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
        and you see two buildings, in one of them is merchant.
        Talk to him.
        """)
    input("Click anything to continue")


def levels(level, inventory, player_x=3, player_y=3):
    """Level inizialization"""
    intro(level)
    game_board = board(20, 60, player_x, player_y)
    game_board = random_buildings(game_board, level)
    while True:
        os.system('clear')
        show_board(game_board)
        inve.print_table(inventory)
        move_variables = movement(game_board, player_x, player_y, inventory)
        game_board = move_variables[0]
        player_x = move_variables[1]
        player_y = move_variables[2]
        inventory = move_variables[3]
        if player_x == 1:
            break


def fun_effectwow():
    """Special effect"""
    f = open("effect.txt", 'r')
    colorlist = ("red", "green", "yellow", "blue", "magenta", "cyan", "white")
    effect_list = [line[:-1] for line in f]
    f.close()
    maxlen = len(effect_list[0])
    for i in range(round(maxlen/2)):
        os.system('clear')
        for z in range(len(effect_list)):
            cprint(effect_list[z][:i+3] + (" " * ((maxlen-i*2)-3)) + effect_list[z][maxlen-i:],
            random.choice(colorlist))
        time.sleep(0.05)


def main():
    """Main function"""
    inventory = {}
    while True:
        os.system('clear')
        fun_effectwow()
        cprint("\n▁▂▄▅▆▇█ FARMER GAME █▇▆▅▄▂▁", 'yellow')
        print("\n1. PLAY\n2. HELP\n3. QUIT\n")
        user_choice = input("You pick: ")
        if user_choice == "1":
            levels(1, inventory)
            levels(2, inventory,1,2)  # 1/1
            levels(3, inventory)
        elif user_choice == "2":
            os.system('clear')
            print("""\nHELP PAGE

        Use W,A,S,D keys to control your hero.
        Press E to talk.
        Go on item to take it.
            """)
            input("Click anything to continue")
        elif user_choice == "3":
            quit()
        else:
            print("Wrong command")
            input()


if __name__ == "__main__":
    main()
