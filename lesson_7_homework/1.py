def changing_types():

    my_list: list[int] = [1, 2, 3, 4, 5]
    new_string_list = list(map(lambda x: str(x), my_list))
    return new_string_list

print(changing_types())

