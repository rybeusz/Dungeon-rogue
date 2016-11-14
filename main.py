def board(x ,y):
    list = []
    for row in range(x):
        list.append([])
        for column in range(y):
            if row == 0
                list[row].append('x')
            else:
                list[row].append('.')
    return lista


def drukowanie_tablicy(lista):
    for i in lista:
        print(''.join(i))


def main():
    drukowanie_tablicy(tablica(15, 10))


if __name__ == "__main__":
    main()
