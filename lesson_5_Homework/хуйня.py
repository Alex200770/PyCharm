def compresses_the_format(main_string):

    count = 1
    result = []

    for i in range(1, len(main_string)):
        if main_string[i] == main_string[i-1]:
            count += 1
        else:
            result.append(main_string[i-1] + str(count))
            count = 1

    result.append(main_string[-1] + str(count))
    #print(result)
    #a = str(result).replace(' ', '').replace('[', '').replace(']', '').replace(',', '').replace("'", "")
    print(*result, sep='')

compresses_the_format(input('Введите строку: '))

def extension_the_format():


    w = []

    main_string = input("Введите строку: ")
    for i in range(1, len(main_string)):
        if i%2 == 0:
            try:
                a += int(main_string[i])
            except ValueError:
                print('Это не число')
        else:
            w.append(main_string[i-1] * a)
            a = 1
    print(w)

extension_the_format()
