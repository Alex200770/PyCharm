from enum import nonmember


class Soda:

    def __init__(self, flavor = None):
        self.flavor = flavor

    def __str__(self):
        if self.flavor:
            if self.flavor.endswith('я'):
                correct_flavor = self.flavor[:-2] + 'ым'
            else:
                correct_flavor = self.flavor
            return f'У вас газировка с {correct_flavor} вкусом'
        else:
            return f'У вас обычная газировка'

W = ['клубничная', 'лимонная', 'фруктовая']

print('   --- Автомат с газировками ---    ')
print('ассортимент -клубничная- -лимонная- -фруктовая-')
your_flavor = input('С каким вкусом вы хотите газировку?: ').lower()

if your_flavor in W:
    soda1 = Soda(your_flavor)
else:
    soda1 = Soda()
print(soda1)

# soda2 = Soda()
# print(soda2)