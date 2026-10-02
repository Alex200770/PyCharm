# s = input('Введите строку: ')

def print_case_counts(s ):
    count_up = 0
    count_low = 0
    for i in s:
        if i.isupper():
            count_up += 1
        if i.islower():
            count_low += 1
    print(f'Букв в верхнем регистре: {count_up}')
    print(f'Букв в нижнем регистре: {count_low}')

print_case_counts(input('Введите строку: '))




