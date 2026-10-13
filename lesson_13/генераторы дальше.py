my_list_comprehension = [i + 1 for i in range(100000) if i % 2 == 0]
# print(my_list_comprehension)

my_gen_exp = [i * 2 for i in range(100000) if i % 2 == 0]
my_gen = my_gen_exp.__iter__()
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())
print(my_gen.__next__())

