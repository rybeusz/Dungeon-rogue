import npc
import inve


def movement(game_board, player_x, player_y, inv):
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
    go_to_next_level = False
    if x in ("w", "s", "a", "d"):
        pos = game_board[player_x + key[x][0]][player_y + key[x][1]]
        if pos == chr(182):  # collecting wheat
            corn = [['corn', 'food', 1]]
            inve.add_to_inventory(inv, corn, 1)
        if pos in ('a', 'b', 'c', 'd', 'e'):  # collecting clothes
            cloth = [['clothes', 'other', 1]]
            inve.add_to_inventory(inv, cloth, 1)
        if pos in ["O", '❤', "☠", "♏", '¢']:  # npc functions
            npc_dict = {"O": 'host', '❤': 'wife', "☠": 'boss', "♏": 'bum', '¢': 'trader'}
            go_to_next_level = getattr(npc, npc_dict[pos])(inv)
        if pos not in special_char:  # moving
            game_board[player_x][player_y] = "."
            game_board[player_x + key[x][0]][player_y + key[x][1]] = "@"
            player_x += key[x][0]
            player_y += key[x][1]

    if x == "x":
        print(inv)
        quit()

    return game_board, player_x, player_y, inv, go_to_next_level
