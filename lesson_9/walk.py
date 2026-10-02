import os

for dirpath, dirnames, filenames in os.walk('.'):
    for dir in dirnames:
        print('Каталог: ', os.path.join(dirpath, dir))

    for file in filenames:
        print('Файлы: ', os.path.join(dirpath, file))
