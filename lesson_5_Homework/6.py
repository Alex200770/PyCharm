l = list(map(int, input('Введите числа через пробел: ').split()))
print('Мы получили список: ', l)
l.sort()
print('Отсортированный список по возрастанию: ', l)
i = int(input('Введите число индексы которого мы будем искать: '))

left, right = 0, len(l) - 1
first_occurrence = -1

# ищем наш индекс числа в левой части списка(находим индекс первого вхождения)

while left <= right:
    mid = (left + right) // 2
    if l[mid] == i:
        first_occurrence = mid
        right = mid - 1
    elif i > l[mid]:
        left = mid + 1
    else: right = mid - 1

# ищем наш индекс числа в правой части списка(находим индекс последнего вхождения)
left, right = 0, len(l) - 1
last_occurrence = -1

while left <= right:
    mid = (left + right) // 2
    if l[mid] == i:
        last_occurrence = mid
        left = mid + 1
    elif i > l[mid]:
        left = mid + 1
    else:
        right = mid - 1

if first_occurrence == -1:
    print('Такого числа нету в нашем списке')
else:
    print(f'Список индексов числа {i}: ', list(range(first_occurrence, last_occurrence + 1)))



# бинарный поиск но мы находим первый попавшийся индекс
# while left <= right:
#     mid = (left + right) // 2
#     if l[mid] == i:
#         print(mid)
#         break
#     if l[left] <= l[right]:
#         if l[left] <= i < l[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1
#     else:
#         if l[mid] < i <= l[right]:
#             left = mid + 1
#         else:
#             right = mid - 1
# else: print('Такого числа нету в списке')



# if duplicates == 1:
#     print(f'Индекс числа {i}: ', end=' ')
# else: print(f'Индексы числа {i}: ', end=' ')
# это просто поиск индекса нашего числа
# for y in range(len(l)):
#     if l[y] == i:
#         print(y, ' ', end='')