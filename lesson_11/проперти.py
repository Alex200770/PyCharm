# class Person:
#     def __init__(self, name):
#         self._name = name
#     @property
#     def name(self):
#         return self._name
#     @name.setter
#     def name(self, value):
#         self._name = value
#     @name.deleter
#     def name(self):
#         self._name = 'Nondefined'
#
#     # name = property(get_name, set_name, del_name)
#
# jack = Person('Jack')
# del jack.name
# jack.name = 'John'
# print(jack.name)
# print(jack.__dict__)


class Creature:
    def __init__(self, height, legs):
        self.height = height
        self.legs = legs

    def run(self):
        print('Creature is running')

    def swim(self):
        print('Creature is swimming')

class Human:
    def __init__(self, money, creature: Creature):
        self.money = money
        self.creature = creature

    def swim(self):
        print('Human is swimming')

creature = Creature(165, 52)
h = Human(0, creature)
h.creature.run()