
def movement(list, player_x, player_y, inv):
    # black magic
    import sys
    import tty
    import termios
    special_char = ["#","O","B",chr(216),"&"]
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        x = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    # end of black magic

    print(x)
    key = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
    if x in ("w", "s", "a", "d"):
        if list[player_x + key[x][0]][player_y + key[x][1]] == '/':
            inv+= 1
        if list[player_x + key[x][0]][player_y + key[x][1]] not in special_char:
            list[player_x][player_y] = "."
            list[player_x + key[x][0]][player_y + key[x][1]] = "@"
            player_x += key[x][0]
            player_y += key[x][1]
        elif list[player_x + key[x][0]][player_y + key[x][1]] == "O":
            
        elif list[player_x + key[x][0]][player_y + key[x][1]] == "B":

        elif list[player_x + key[x][0]][player_y + key[x][1]] == chr(216):


    if x == "x":
        print(inv)
        quit()

    return list, player_x, player_y, inv
