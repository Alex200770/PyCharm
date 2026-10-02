def first_and_last_occurrence(l):

    #l = list(map(int,input('Введите числа через пробел: ').split()))
    print('Мы получили список: ', l)
    l.sort()
    print('Отсортированный список по возрастанию: ', l)
    i = int(input('Введите число, индексы которого вы хотите найти: '))
    #бинарным поиском найдем индексы нашего числа

    left, right = 0, len(l) - 1
    first = -1

    #ищем по левой части
    while left <= right:
        mid = (left + right) // 2
        if l[mid] == i:
            first = mid
            right = mid - 1
        elif i > l[mid]:
            left = mid + 1
        else:
            right = mid - 1

    left, right = 0, len(l) - 1
    last = -1

    #ищем по правой части
    while left <= right:
        mid = (left + right) // 2
        if  l[mid] == i:
            last = mid
            left = mid + 1
        elif i > l[mid]:
                left = mid + 1
        else:
            right = mid - 1
            
    if first == -1:
        print('Такого числа нету в списке')
    else: print(f'Список индексов числа {i}: ', list(range(first, last + 1)))

first_and_last_occurrence(list(map(int,input('Введите числа через пробел: ').split())))
