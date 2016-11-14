import os


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


def show_board(lista):
    for i in lista:
        print(''.join(i))


def move(list, player_x, player_y):
    import sys
    import tty
    import termios
    special_char = ('#')
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    x = ch
    print(x)
    if x == 'w' and (list[player_x-1][player_y] not in special_char):
        list[player_x][player_y] = "."
        player_x -= 1
        list[player_x][player_y] = "@"
    elif x == 's' and (list[player_x+1][player_y] not in special_char):
        list[player_x][player_y] = "."
        player_x += 1
        list[player_x][player_y] = "@"
    elif x == 'a' and (list[player_x][player_y-1] not in special_char):
        list[player_x][player_y] = "."
        player_y -= 1
        list[player_x][player_y] = "@"
    elif x == 'd' and (list[player_x][player_y+1] not in special_char):
        list[player_x][player_y] = "."
        player_y += 1
        list[player_x][player_y] = "@"

    return list, player_x, player_y


def main():
    player_x = 3
    player_y = 3
    game_board = board(15, 50, player_x, player_y)

    while True:
        os.system('clear')
        show_board(game_board)
        zwrot = move(game_board, player_x, player_y)
        game_board = zwrot[0]
        player_x = zwrot[1]
        player_y = zwrot[2]
        if input("press x to exit") == "x":
            break


if __name__ == "__main__":
    main()
