import npc
import inve


def movement(list, player_x, player_y, inv):
    # black magic
    import sys
    import tty
    import termios
    special_char = ['█', "O", '❤', "☠", "&", "♏", '¢']
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        x = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    # end of black magic
    key = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
    if x in ("w", "s", "a", "d"):
        if list[player_x + key[x][0]][player_y + key[x][1]] == chr(182):  # collecting wheat
            corn = [['corn', 'food', 1]]
            inve.add_to_inventory(inv, corn, 1)
        if list[player_x + key[x][0]][player_y + key[x][1]] in ('a', 'b', 'c', 'd', 'e'):  # collecting clothes
            cloth = [['clothes', 'other', 1]]
            inve.add_to_inventory(inv, cloth, 1)
        if list[player_x + key[x][0]][player_y + key[x][1]] not in special_char:
            list[player_x][player_y] = "."
            list[player_x + key[x][0]][player_y + key[x][1]] = "@"
            player_x += key[x][0]
            player_y += key[x][1]
        if list[player_x + key[x][0]][player_y + key[x][1]] in ["O", '❤', "☠", "♏", '¢']:
            npc_dict = {"O": 'host2', '❤': 'wife1', "☠": 'boss', "♏": 'menel', '¢': 'trader'}
            getattr(npc, npc_dict[list[player_x + key[x][0]][player_y + key[x][1]]])(inv)

    if x == "x":
        print(inv)
        quit()

    return list, player_x, player_y, inv
