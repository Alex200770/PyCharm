def do_summ(a: int, b: int, ) -> int:
    return a + b

def do_div(a: int, b: int) -> int:
    return a // b

def foo():
    try:
        a = int(input('Number a: '))
        b = int(input('Number b: '))
        if b == 0:
            raise ZeroDivisionError('Не дели на ноль')
        return 999
    except Exception as e:
        print(f'Some error happened: {e}')
    else:
        print('В этот раз без ошибок')
    finally:
        print('Блок finally')

# try:
#     print('1' + 1)
# except TypeError:
#     raise