import os
# from os import *
print(os.path.exists('кодировка.py'))
print(os.path.exists('кодировка2.py'))

path_to_file = os.path.join('lesson_9', 'OS.py')
print(path_to_file)
# print(os.path.exists(path_to_file))
# os.makedirs(os.path.join('new', 'new1', 'new2'))

# root_dir = os.path.join('new')
# print(next(os.walk(root_dir)))
# os.replace('Alex.py', 'new/Alex.py')
#
# os.rename('main.py', 'Alex.py')

# for obj in os.listdir('new'):
#     if obj.__name__ == 'new1':
#         for o in obj:
#             print(o)