def get_marks(main_file: str, lesser_file: str):

    errors = []

    with open(main_file, 'r', encoding='utf-8') as file1:
        with open(lesser_file, 'w', encoding='utf-8') as file2:
                count = 0
                for i in file1:
                    count += 1
                    a = i.split()
                    marks = int(a[-1])
                    name = ' '.join(a[:-1])
                    if marks > 10 or marks < 1:
                        errors.append(f'Ошибка в строке {count}: {marks} - оценка должна быть 1-10')
                        continue
                    if marks < 3:
                        file2.write(f'{name} - {marks}\n')
                        print(name, '-', marks)
    return errors

with open('main_file.txt', 'w', encoding='utf-8') as text1:
    text1.write('Миткевич Алексей 18\nСтаравойтова Екатерина 12\nИванов Иван 1\nПупкин Петя 7\nФамилия Имя 2')

errors = get_marks('main_file.txt', 'lesser_file.txt')
print(*errors, sep='\n')

# def get_marks(main)