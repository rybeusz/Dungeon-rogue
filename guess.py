import random

def user_choice():
    """ask for number and check if its int with right len"""
    while True:
        try:
            user_input = input('\nchoose your number, member if u guess right u will win Titanic ticket: ')
            if len(user_input) == 3 and type(int(user_input)) == int:
                return tuple(map(int, user_input))
        except:
            pass




def random_number():
    """return random number"""
    return tuple(random.sample(range(1,10),3))


def main(vodka):
    """start game with amount of vodka in your backpack"""
    i = vodka * 2
    drawn = random_number()
    print(drawn)
    while i > 0:
        user = user_choice()
        i -= 1
        if set(drawn).intersection(user):
            for z in range(3):
                if (user[z] in drawn) and (user[z] == drawn[z]):
                    print("\033[91m {}\033[00m".format('hot'), end=' ')
            for f in range(3):
                if (user[f] in drawn) and (user[f] != drawn[f]):
                    print("\033[93m {}\033[00m".format('warm'), end=' ')
            if user == drawn:
                print('\x1b[10;33;41m'+ '\nYou win titanic ticket nice!' + '\x1b[0m')
                quit()
        else:
            print("\033[94m {}\033[00m".format('cold'), end=' ')


if __name__ == '__main__':
    main()
