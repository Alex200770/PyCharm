def find_nod(e,f):

    while f != 0:
        k = e % f
        e = f
        f = k
    print(e)

find_nod(int(input('Введите первое число: ')), int(input('Введите второе число: ')))
