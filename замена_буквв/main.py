#import this

def change_string():

    line = input('Введите строку: ')
    line = line[0] + line[1:-1].replace('h', 'H') + line[-1]
    print(line)

change_string()