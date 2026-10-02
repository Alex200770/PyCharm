#name = input('Привет, напиши свое имя: ')
#print(name.capitalize())
#print(name[0])
#print(name[::-1])
#print(name.title())

#user_name = "Alex"
#user_age = 20
#result = user_age + 5
#print(user_name, result)

# изменяемые
print(type([1, '3', True]))
print(type({1, 2, 3}))

# неизменяемые
print(type(5)) #int
print(type(True)) #bool
print(type((1, 2, 3)))

#my_list = [1, '3', True]
#print(type(my_list[1]))

a = [1, 2, 3]
print(id(a))

a.append(4)

print(a)
print(id(a))

a = 4
print(id(a))
a = 6
print(id(a))
print('')

a = [1, 2]
b = [1, 2]
f = a
print(f)
#print(a == b)
#print(a is b)
print()

c = 200
h = 200
print(c is h)
print()

text = 'Hello, world!'
print(text.find('l'))
print(text[0:6])
print()

#фильтрация
list_of_books = {1, 2, 3, 2, 2, 4, 4, 7}
unique_list_of_books = set(list_of_books)
print(unique_list_of_books)



