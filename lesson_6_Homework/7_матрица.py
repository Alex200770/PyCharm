import random

m = int(input('Введите длину матрицы: '))
n = int(input('Введите ширину матрицы: '))

for i in range(m):
    for j in range(n):
        rand = random.randint(1, 12)
        if rand < 10: print(' ', rand, end=' ')
        else: print('', rand, end=' ')
    print()