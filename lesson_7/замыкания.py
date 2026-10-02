from typing import Callable

def outer_function(l: list[int]) -> Callable:
    def inner_function(number: int) -> list[int]:
        l.append(number)
        return l
    return inner_function

closure = outer_function([1, 2, 3])
print(closure(4))
print(closure(4))
print(closure(5))



print()


def format_output(func):
    def inner(arg):
        print('*' * 10)

        func(arg)

        print('*' * 10)
    return inner

@format_output
def greeting():
    print('hello')


@format_output
def power(n):
    print(n ** 2)

power(4)
#greeting()