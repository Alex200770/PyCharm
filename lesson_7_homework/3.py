def find_palindromes():

    my_list: list[str] = ['level', 'noon', 'madam', 'kate', 'fuck']
    new_list = list(filter(lambda x: x == x[::-1], my_list))
    return new_list

print(find_palindromes())