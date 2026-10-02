# import this
import time

def decorate_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f'Время: {time.time() - start:.10f} секунд')
        return result
    return wrapper


@decorate_time
def find_palindromes():

    my_list: list[str] = ['level', 'noon', 'madam', 'kate', 'fuck']
    new_list = list(filter(lambda x: x == x[::-1], my_list))
    return new_list

print(find_palindromes())