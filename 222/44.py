l = list(map(int, input('Введите числа через пробел: ').split()))
print('У нас получился список: ', l)
print('Сумма элементов списка: ', sum(l))

minimum = l[0]
maximum = l[0]

for i in l:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i

print('Минимальное значение: ', minimum)
print('Максимальное значение: ', maximum)