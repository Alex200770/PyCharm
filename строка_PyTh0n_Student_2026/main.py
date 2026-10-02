#import this

def work_with_strings():

    line = input('Введите строку: ')

    print(line.lower(), '(В нижнем регистре)')
    print(len(line), '(Длина строки)')
    print(line[0:6], '(Первые 6 символов)')
    print(line[0:6].lower(), '(Первые 6 символов в регистре)')
    print(line.lower().count('t'), "(Количество символов 't' без учета регистра)")

    result = line.replace(" ", '').replace("Student", 'Developer')
    print(result)

work_with_strings()