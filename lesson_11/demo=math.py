class IntCompatible:

    def __init__(self, value):
        self.value = value

    def __mul__(self, number):
        return self.value * number

    def __floordiv__(self, number):
        return self.value // number

    def __truediv__(self, number):
        return self.value / number

    def __sub__(self, number):
        return self.value - number

a = IntCompatible(100)
b = 20

print(a // b)
print('a' * 3)