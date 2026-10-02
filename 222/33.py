print('Числа Фибоначчи')
first_number = int(input('Введите первое число: '))
k = int(input('Длина последовательности: '))

second_number = first_number

for i in range(k):
    print(first_number, end=' ')
    x = first_number
    first_number = second_number
    second_number = x + first_number

