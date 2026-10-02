#import this

def calculating_body_mass_index(height: float, weight: float) -> float:
    mass_index = weight / (height ** 2)

    if height <= 0.5 or weight <= 10 or height > 2.5 or weight >= 250: #на случай если человек введет бред
        raise ValueError('Вы ввели некоректные значения')
    if mass_index <= 16:
        print('Выраженный дефицит массы тела')
    if 16 < mass_index <= 18.5:
        print('Недостаточная(дефицит) масса тела')
    if 18.5 < mass_index <= 25:
        print('Норма')
    if 25 < mass_index <= 30:
        print('Избыточная масса тела(предожирение')
    if 30 < mass_index <= 35:
        print('Ожирение первой степени')
    if 35 < mass_index <= 40:
        print('Ожирение второй степени')
    if mass_index > 40:
        print('Ожирение третьей степени')
    return mass_index

try:
    user_height = float(input('Введите рост в метрах: '))
    user_weight = float(input('Введите вес в килограммах: '))
    result = calculating_body_mass_index(user_height, user_weight)
    print(f'Расчет ИМТ: {result:.2f}')
except ValueError as e:
    print(f'Произошла ошибка: {e}')
