import os


def board(x, y):
    """Create a board"""
    list = []
    for row in range(x):
        list.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                list[row].append('#')
            else:
                list[row].append('.')
    return list


def show_board(lista):
    for i in lista:
        print(''.join(i))


def move(list):
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    x = ch
    print(x)

    if x == 'w':
        pass
    if x == 's':
        pass
    if x == 'a':
        pass
    if x == 'd':
        pass

    return list


def main():
    game_board = board(15, 50)

    while True:
        os.system('clear')
        show_board(game_board)
        game_board = move(game_board)
        if input("press x to exit") == "x":
            break


if __name__ == "__main__":
    main()
