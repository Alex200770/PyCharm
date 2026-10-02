l = list(map(int, input('Введите числа через пробел: ').split()))
print('У нас получился список: ', l)

duplicates = 0
w = []

for i in l:
    a = l.count(i)
    if a > 1:
        duplicates += 1
        if i not in w:
            print(f'Число {i} встречается {a} раз')
            w.append(i)

if duplicates == 0:
    print('Все числа уникальны')
else: print()