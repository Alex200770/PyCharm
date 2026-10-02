# city = "New York"
#
# print('=' * 40)
# users_guess = input('Привет, отгадай город, который я загадал: ')
#
#
# if users_guess.lower() == city.lower():
#     print('Ты угадал')
# elif users_guess == 'Miami':
#     print(f'Нет, это не {users_guess}, но хорошая попытка')
# elif users_guess == 'Hamburg':
#     print(f'Нет, это не {users_guess}, совсем не рядоа')
# else:
#     print('Попробуй еще раз')


#тернарный апператор
num_a = 5
num_b = 12

result = num_a if num_a > num_b else num_b

# if num_a > num_b:
#     result = num_a
# else:
#     result = num_b

print(result)
