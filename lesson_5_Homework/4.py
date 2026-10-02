#import this

#list_1 = [2, 5, 1, 6, 9, 4, 7]
list_2 = list(map(int, (input('Введите числа через пробел: ')).split()))
#print(type(list_2))
minimum = list_2[0]
maximum = list_2[0]

print(sum(list_2))

for i in list_2:
    if i < minimum:
        minimum = i
    if i > maximum:
        maximum = i

print('Минимальный элемент: ', minimum)
print('Максимальный элемент: ', maximum)

