from collections import defaultdict

# my_defdict = defaultdict(int)
# my_defdict['a'] = 1
#
# print(my_defdict['a'])
# print(my_defdict['key'])

# dictionary = {}
# key = "a"
# value = 1

# dictionary.setdefault(key, []).append(value)
# dictionary['a'].append(2)
#
# # if key not in dictionary:
# #     dictionary[key] = []
# # dictionary[key].append(value)
#
# print(dictionary)


#обьединение и распаковка словорей | |= **
# print(hash('100'))
# print(hash('100'))
# def connect(host, port, timeout):
#     print(host, port, timeout)
#
# connect(host='localhost', port=443, timeout=30)
# config = {
#     'name': 'Alex',
#     'age': 20,
# }
# updated_user = {
#     **config,
#     'age': 30,
# }
# print(updated_user)
# a = {'x': 1, 'y': 2}
# b = {'y': 100, 'z': 3}

# a |= b
# print(a)

# c = a | b
# print(c)

#сортировка
# my_list: list[int] = [10, 14, 7, 0]
# my_sorted_list = sorted(my_list)
# print(my_list)
# print(my_sorted_list)


# data = {'b': 2, 'a': 1, 'c': 3}
# sorted_data = dict(sorted(data.items())) #items чтобы и значения были
# # и dict чтобы был словарь как изначально
#
# print(sorted_data)

#Counter
# from collections import Counter
#
# languages: list[str] = ['python', 'java', 'python', 'go', 'python']
# counts = Counter(languages)
#
# most_common_languages = counts.most_common()[0][0]
# print(most_common_languages)
# print(counts['python'])
# print(counts)


# dict.fromkeys()

m = ['a', 'b', 'c']

# my_dict = dict.fromkeys(keys, 100) #из ключей создать список дикт
# print(my_dict)

d = {key: [] for key in m}
d['a'].append(10)
d['c'].append(20)
print(d)