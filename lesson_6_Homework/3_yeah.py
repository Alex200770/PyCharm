def number(n):

    for i in range(2, n):
        if n % i == 0:
            print(f'Число {n} составное')
            break
        else:
            print(f'Число {n} простое')
            break

number(int(input('Введите число: ')))