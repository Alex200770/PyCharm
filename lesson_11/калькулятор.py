class Math:

    def addition(self, a, b):
        print(f'{a} + {b} = {a + b}')
    def subtraction(self, a, b):
        print(f'{a} - {b} = {a - b}')
    def multiplication(self, a, b):
        print(f'{a} * {b} = {a * b}')
    def division(self, a, b):
        if b == 0:
            print('ERROR! На ноль делить нельзя')
        else:
            print(f'{a} : {b} = {a / b}')

my_math = Math()
my_math.addition(4, 5)
my_math.subtraction(4, 5)
my_math.multiplication(4, 5)
my_math.division(4, 5)
my_math.division(4, 0)