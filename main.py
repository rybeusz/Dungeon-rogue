def tablica(x=5, y=5):
    lista = []
    for rzad in range(x):
        lista.append([])
        for kolumn in range(y):
            if rzad == 0 or rzad == x-1 or kolumn == 0 or kolumn == y-1:
                lista[rzad].append('x')
            else:
                lista[rzad].append('.')
    return lista


def drukowanie_tablicy(lista):
    for i in lista:
        print(''.join(i))


def main():
    drukowanie_tablicy(tablica(15, 10))


if __name__ == "__main__":
    main()
