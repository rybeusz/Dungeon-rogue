import random
import sys
import time


class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    Default = '\033[99m'


def user_guess():
    """user guesss"""

    while True:
        try:
            user_guess = int(input('guess: '))
            if 100 <= user_guess < 1000:
                return list(str(user_guess))
        except:
            pass


def random_number():
    random_number = random.randint(100, 999)
    random_number = list(str(random_number))
    return random_number


def main():
    """main function"""
    rand_number = random_number()
    print(rand_number)
    count = 0

    while True:
        start_time = time.time()

        guess_number = user_guess()
        count += 1
        if rand_number == guess_number:
            print(bcolors.OKGREEN + 'win' + bcolors.ENDC)
            end_time = time.time()
            print('Your time', int(end_time - start_time), 'Your count: ', count)

            while True:
                question = input('again y/n: ')
                if question.lower() == 'y':
                    main()
                elif question.lower() == 'n':
                    quit()
                else:
                    continue

        elif not set(rand_number) & set(guess_number):
            print(bcolors.WARNING + 'cold' + bcolors.ENDC)

        elif (rand_number[0] == guess_number[0]) or (rand_number[1] == guess_number[1]) or (
            rand_number[2] == guess_number[2]):
            print(bcolors.FAIL + 'hot' + bcolors.ENDC)

        else:
            print(bcolors.WARNING + 'warm' + bcolors.ENDC)


main()

if __name__ == '__main__':
    main()