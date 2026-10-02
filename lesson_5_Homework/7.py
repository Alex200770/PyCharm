l = list(map(int, input('Введите числа через пробел: ').split()))
print('У нас получился список: ', l)
# сортировка по возрастанию
l.sort()
print('Отсортированный список по возрастанию: ', l)

k = int(input('Введите число от которого мы будем сдвигать вправо: '))
l2 = l[k:-1] + [l[-1]] + l[0:k]

print('Новый список: ', l2)

f = int(input('Введите число индекс которого вы хотите найти: '))

left, right = 0, len(l) - 1
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
else: print('Нету такого числа в списке')


