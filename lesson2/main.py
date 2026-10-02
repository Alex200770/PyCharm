#import this
print('Hello, World')
print('It is my first python program')
print('And it is the end of program')
print('Bye-bye')
print(' ')

def data():
    a = input('Привет, как тебя зовут? : ')
    print('Супер, мы теперь знакомы!')
    b = input('А в каком городе ты живешь? : ')
    print('Классный город!')
    c = input('А чем ты увлекаешься? : ')
    print('Ого... это крутяк!')

    print('Данные о тебе')
    print('твое имя -',a )
    print('Место проживания -', b)
    print('Увлечения -', c)

data()

print('')

def new_year():
    a = int(input('Какой сейчас год? : '))
    result = a + 1
    print('Скоро будет',result)

new_year()

