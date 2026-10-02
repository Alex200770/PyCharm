from typing import Callable

def cache(func: Callable) -> Callable:
    cache: dict[int, list[int]] = {}
    def inner(arg: int):
        result = cache.get(arg)
        if not result:
            print('интерпретатор был тут')
            result = func(arg)
            cache[arg] = result
        return result
    return inner


@cache
def make_list(num: int) -> list[int]:
    num_list = [n for n in range(1, num + 1)]
    #for n in range(1, num + 1):
        #num_list.append(n)

    return num_list

print(make_list(10), end='\n\n')
print(make_list(10))