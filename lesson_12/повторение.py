from copy import deepcopy


class Workers:
    def __init__(self, workers_list: list[str]) -> None:
        self.__workers_list = deepcopy(workers_list) #это мы сделали копию

    def __str__(self) -> str:
        return str(self.__workers_list)

    def __isub__(self, other: str) -> 'Workers': #удаляем
        self.__workers_list.remove(other) #если по индексу то .pop()
        return self

    def __iadd__(self, other: str) -> 'Workers':#добавляем
        self.__workers_list.append(other)
        return self

    def __contains__(self, item: str) -> bool:
        return True if item in self.__workers_list else False

list_of_workers = ['Anna', 'Alex', "Mark", ['Kate']]
workers_obj = Workers(list_of_workers)

print(list_of_workers)
print(workers_obj)
print()

workers_obj += 'William'
print(list_of_workers)
print(workers_obj)
print()

list_of_workers[-1].append('Jack')
print(list_of_workers)
print(workers_obj)
print()

# workers_obj -= 'Anna'
# print(workers_obj)
#
# workers_obj += 'John'
# print(workers_obj)
#
# print('John' in workers_obj)
# print('Anna' in workers_obj)