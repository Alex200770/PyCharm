print('Числа Фибоначчи', end=' ->\n')

first_number = int(input('Введите первое число: '))
n = int(input('Сколько чисел ввести: '))

second_number = first_number

for i in range(n):
    print(first_number, end=' ')
    x = first_number
    first_number = second_number
    second_number = x + second_number

