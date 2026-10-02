def make_a_calculator(first_number: float, second_number: float) -> float:

    print('Доступные операции')
    print('+ : Сложение')
    print('- : Разность')
    print('* : Умножение')
    print('/ : Деление')
    print('** : Возведение в степень')

    a = input('Введите операцию: ')

    if a == '+':
        return first_number + second_number
    elif a == '-':
        return first_number - second_number
    elif a == '*':
        return first_number * second_number
    elif a == '/':
        if second_number != 0:
            return first_number / second_number
        else:
            return "На ноль делить нельзя"
    elif a == '**':
        return first_number ** second_number
    else:
        return "Неизвестная операция"

try:
    user_first_number = float(input('Введите первое число: '))
    user_second_number = float(input('Введите второе число: '))
    result = make_a_calculator(user_first_number, user_second_number)
    if isinstance(result, (int, float)):
        print(f'Результат: {result:.3f}')
    else:
        print(result)
except ValueError as e:
    print(f'Произошла ошибка: {e}')