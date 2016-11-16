import random

def user_choice():
    try:
        user_input = input('\nchoose your number: ')
        if len(user_input) == 3 and type(int(user_input)) == int:
            return tuple(map(int, user_input))
    except:
        pass


def random_number():
    return tuple(random.sample(range(1,10),3))


def main():
   # print(random_number())
    i = 0
    drawn = random_number()
    print(drawn)
    while i < 10:
        user = user_choice()
        if set(drawn).intersection(user):
            for z in range(3):
                if (user[z] in drawn) and (user[z] == drawn[z]):
                    print('hot', end=' ')
            for f in range(3):
                if (user[f] in drawn) and (user[f] != drawn[f]):
                    print('warm', end=' ')
        else:
            print('cold', end=' ')


if __name__ == '__main__':
    main()
