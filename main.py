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


def show_board(list):
    for i in list:
        print(''.join(i))


def move(list, player_x, player_y):
    # black magic
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
    # end of black magic

    x = ch  # x is inputed character
    print(x)
    key = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}

    if x in ("w", "s", "a", "d"):
        if list[player_x + key[x][0]][player_y + key[x][1]] not in special_char:
            list[player_x][player_y] = "."
            list[player_x + key[x][0]][player_y + key[x][1]] = "@"
            player_x += key[x][0]
            player_y += key[x][1]
    if x == "x":
        quit()

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


if __name__ == "__main__":
    main()
