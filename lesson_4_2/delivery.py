import rates

carm_sum = float(input('Введите сумму корзины: '))

total = carm_sum + rates.delivery_fee

print('Сбор за доставку: ', rates.delivery_fee)
print('Итог к оплате: ', total)