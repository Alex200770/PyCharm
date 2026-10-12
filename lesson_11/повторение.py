import math

SUPER_NUMBER = 16

class MyClass(str):
    def __init__(self, arg1: int) -> None:
        self.argument = arg1
        self.__arg = SUPER_NUMBER

    def __do_inner_logic(self):
        print('hello') # это не действие а данные поэтому и нету в дикте

class MyClass2(MyClass):
    def __init__(self, arg1: int) -> None:
        super().__init__(arg1)

    def do_something(self, number):
        return self.argument * number

my_instance = MyClass2(10)
print(my_instance.argument)
# my_instance = MyClass('MyClass instance')
# # my_instance.__arg #пайтон обсфуцирует то есть прячет от нас
# print(my_instance.__dict__) #на собесе про память/ каждый обьект носит дикт

