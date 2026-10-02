#import this

def work_with_strings():

    line = input('Введите строку: ')

    print(line[2])      #1
    print(line[-2])     #2
    print(line[0:5])    #3
    print(line[0:-2])   #4
    print(line[::2])    #5
    print(line[1::2])   #6
    print(line[::-1])   #7
    print(line[::-2])   #8
    print(len(line))    #9

work_with_strings()