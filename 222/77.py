l = list(map(int, input('Введите числа через пробел: ').split()))
print('У нас получился список: ', l)
l.sort()
print('Отсортированный список по возрастанию: ', l)
k = int(input('Введите число из списка: '))
l2 = l[k:-1] + [l[-1]] + l[0:k]
print(f'Сдвинутый список по числу {k}: ', l2)

f = int(input('Индекс какого числа будем искать: '))
left, right = 0, len(l) - 1

duplicates = l2.count(f)
if duplicates >= 1:
    print(f'Индекс числа {f}: ', end='')

while left <= right:
    mid = (left + right) // 2
    if l2[mid] == f:
        print(mid)
        break
    if l2[left] <= l2[mid]:
        if l2[left] <= f < l2[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if l2[mid] < f <= l2[right]:
            left = mid + 1
        else:
            right = mid - 1
else: print('Нету такого числа')
