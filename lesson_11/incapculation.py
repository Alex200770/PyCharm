class Computer:
    def __init__(self, price):
        self.__price = price


computer = Computer(10_000)
print(computer.__dict__)
print(computer._Computer__price)