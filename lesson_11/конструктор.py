class Car(object):
    def __init__(self, color, km):
        self.color = color
        self.km = km

    def __del__(self):
        print(f'object of class {self.__class__.__name__} with km={self.km} has been deleted')
mazda = Car('red', 0)
mercedes = Car('grey', 100000)

del mercedes

print(mazda.color)
# print(mercedes.color)