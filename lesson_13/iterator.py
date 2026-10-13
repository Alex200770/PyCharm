a = [1, 2] #итерируемый обьет
b = a.__iter__() #итератор
c = b.__next__()
b.__next__()

j = a.__iter__()
print(id(b), id(j))
print('j next', j.__next__())
print('j next', j.__next__())

try:
    j.__next__()
except StopIteration:
    print('Our iterator is exhausted')