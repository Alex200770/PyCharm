N = int(input('Стоимость телефона: '))
k = int(input('Сколько Маша будет откладывать каждый день кроме воскресенья: '))

days = 0
total = 0

while N > total:
    days += 1
    if days % 7 != 0:
        total += k
print('За столько дней накопит: ', days)