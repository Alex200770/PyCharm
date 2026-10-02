def changing_types():

    my_list: list[int] = [-2, -1, 0, 1, 2, 3, 4]
    new_list = list(filter(lambda x: x > 0, my_list))
    return new_list

print(changing_types())