# def divide(a, b):
#     return a // b
#
# result = divide(b=5, a=10)
# print(result)
#
# extra_name = 'Alex'
# def print_names(*names):
#     for name in names:
#         print(name)
#     print(extra_name)
#     print(locals())
#
# print_names('James', 'Rick', 'Luke')
#
# print(globals())

from typing import Any

extra_name: str = 'Alex'
print(extra_name)

def print_something(names: list[Any]) -> int:
    print(names)
    return 2