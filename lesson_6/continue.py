# list_of_numbers = [1, 2, 3, 4, 5]
#
# for i in list_of_numbers:
#     if i == 3:
#         continue
#     print(i)

l = list(map(int, input(': ').split()))
l.sort()
number = int(input("Введи число, индекс которого хочешь получить: "))

left, right = 0, len(l) - 1
first_occurrence = -1
while left <= right:
        mid = (left + right) // 2
        if l[mid] == number:
            first_occurrence = mid
            right = mid - 1
        elif l[mid] < number:
            left = mid + 1
        else:
            right = mid - 1


left, right = 0, len(l) - 1
last_occurrence = - 1

while left <= right:
    mid = (left + right) // 2
    if l[mid] == number:
        last_occurrence = mid
        left = mid + 1
    elif l[mid] > number:
        right = mid - 1
    else:
        left = mid + 1

if first_occurrence == -1:
    print('nooo')
else:
    print(f'Список индексов числа: ', list(range(first_occurrence, last_occurrence + 1)))
