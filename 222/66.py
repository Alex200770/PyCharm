l = list(map(int, input('Введите числа через пробел: ').split()))
print('У нас получился список: ', l)

l.sort()
print('Отсортированный список по возрастанию: ', l)

f = int(input('Введите число: '))

duplicates = l.count(f)
if duplicates == 1:
    print(f'Индекс числа {f}: ', end=' ')
else: print(f'Индексы числа {f}: ', end=' ')

for i in range(len(l)):
    if l[i] == f:
        print(i, end=' ')