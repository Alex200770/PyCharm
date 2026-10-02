# 5! = 1 * 2 * 3 * 4 * 5

# def find_factorial(number: int) -> int:
#     if number == 0:
#         return 1
#
#     return number * find_factorial(number - 1)




def find_factorial(number: int) -> int:
    total: int = 1
    for num in range(1, number + 1):
        total *= num

    return total


print(find_factorial(5))