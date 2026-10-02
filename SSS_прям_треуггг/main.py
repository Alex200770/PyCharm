#import this

def calculation_of_area():

    print('Находим площадь прямоугольного треугольника и его гипотенузу')

    cat_a = int(input('Введите значение первого катета: '))
    cat_b = int(input('Введите значение второго катета: '))

    result1 = 0.5 * (cat_a * cat_b)
    print('Площадь прямоугольного треугольника равна: ', result1)

    result2 = (cat_a ** 2 + cat_b ** 2) ** 0.5
    print('Значение гипотенузы: ', result2)

calculation_of_area()