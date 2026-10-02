#import this

import math

print('Задание 1\n')

def learn_module_math():

    a = float(input('Введите значение переменной а: '))
    b = float(input('Введите значение переменной b: '))
    x = float(input('Введите значение переменной x: '))

    print('Даны следующие пункты', end=" ->\n")
    print("1)", 'y = (a^2)/3 + (a^2 + 4)/b + (sqrt(a^2 + 4))/4 + (sqrt((a^2 + 4)**3))/4')
    print("2)", 'y = cos(x) + sin(x)')
    print("3)", 'y = pow(pow((cos(x^2))^2 + (sin(2x-1))^2, 1/3)')
    print("4)", 'y = 5x + 3x^2 * sqrt(1 + (sin(x))^2)')


    number = (input('Какое выражение вы хотите посчитать? '))
    if number == '1':
        print((pow(a, 2))/3 + (pow(a, 2) + 4)/b + (math.sqrt(pow(a, 2) + 4))/4 + (math.sqrt(pow(pow(a, 2) + 4, 3)))/4)
    elif number == '2':
        print(math.cos(x) + math.sin(x))
    elif number == '3':
        print(pow(pow(math.cos(pow(x, 2)), 2) + pow(math.sin(2*x - 1), 2), 1/3))
    elif number == '4':
        print(5*x + 3*pow(x, 2) * math.sqrt(1 + pow(math.sin(x), 2)))
    else:
        print('Нету такого номера')

learn_module_math()

print('\n')
print('Задание 2')

def played_with_loans_lost():

    print('Рассчет размера ежемесячной выплаты кредита', end=' ->\n')
    print('╔════════════════════════════════════════════════╗')
    print('║ i - годовая процентная ставка                  ║')
    print('║ p - месячная процентная ставка                 ║')
    print('║ s - сумма займа                                ║')
    print('║ n - количество месяцев, на которые взят кредит ║')
    print('╚════════════════════════════════════════════════╝')
    print()
    i = float(input('i = '))
    s = float(input('s = '))
    n = float(input('n = '))
    p = (pow(1+i/100, 1/12) - 1)
    print('месячная процентная ставка: ', p)
    m = (s * p * pow(1+p, n)) / (pow(1+p, n) - 1)
    print('ежемесячная выплата: ', m)
    print('конечная сумма выплаты банку: ', m * n)
    print('переплата банку: ', m * n - s)

played_with_loans_lost()

print('\n')
print('Задание 3')

def interstellar():

    print('╔═════════════════════════════════════╗')
    print('║ R1 - радиус орбиты планеты 1        ║')
    print('║ R2 - радиус орбиты планеты 2        ║')
    print('║ W1 - орбитальная скорость 1 планеты ║')
    print('║ W2 - орбитальная скорость 2 планеты ║')
    print('╚═════════════════════════════════════╝')

    R1 = float(input('R1 = '))
    R2 = float(input('R2 = '))
    W1 = float(input('W1 = '))
    W2 = float(input('W2 = '))

    L1 = (2*R1*math.pi)/W1
    L2 = (2*R2*math.pi)/W2

    print("Длина года на 1 планете: ", L1)
    print("Длина года на 2 планете: ", L2)

    if L1 > L2:
        print('True')
    else:
        print('False')

interstellar()
