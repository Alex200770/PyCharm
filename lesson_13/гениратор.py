my_list_comprehension = [i + 1 for i in range(10) if i % 2 == 0]
my_set_comprehension = {i + 1 for i in range(10) if i % 2 == 0}
print(type(my_list_comprehension))
print(type(my_set_comprehension))
print('=' * 55)

my_generator_expression = [i + 1 for i in range(10) if i % 2 == 0]
print(my_generator_expression)

for i in my_generator_expression:
    print(i)

