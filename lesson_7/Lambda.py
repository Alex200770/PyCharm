from functools import reduce
# def power(x: int) -> int:
#     return x ** 2

my_list: list[int] = [1, 2, 3, 4]
#print(list(map(power, my_list)))
#print(list(map(lambda x: x ** 2, my_list)))
print(reduce(lambda x, y: x * y, my_list, 2))