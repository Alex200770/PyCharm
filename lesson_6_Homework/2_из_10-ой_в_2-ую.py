def ten_in_two(number):

    w = []

    while number > 0:
        k = number % 2
        if k == 0:
            w.append(0)
        elif k == 1:
            w.append(1)
        number = number // 2
    print(*w, sep='')

ten_in_two(int(input('Введите число: ')))
