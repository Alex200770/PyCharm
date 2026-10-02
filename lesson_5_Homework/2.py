#import this

price_of_smartphone = float(input('Цена смартфона: '))
k = float(input('Сколько маша откладывает денег в день: '))

days = 0 #сколько дней будет копить
total = 0 #накопления

while price_of_smartphone > total:
    if k == 0:
        print('Маша не накопит')
        break
    days += 1
    if days % 7 != 0:
        total += k


if k > 0: print('За сколько дней накопит: ', days)

