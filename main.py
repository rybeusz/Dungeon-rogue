def board(x, y):
    list = []
    for row in range(x):
        list.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                list[row].append('#')
            else:
                list[row].append('.')
    return list


def drukowanie_tablicy(lista):
    for i in lista:
        print(''.join(i))

def move(list):
    pass

def getch():
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

x = getch()
print(x)

def main():
    drukowanie_tablicy(board(15, 50))


if __name__ == "__main__":
    main()
