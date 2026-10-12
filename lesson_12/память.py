# config = {'there': 'dark', 'autosave': True}
# my_list = [1, 2, 3]
# default = ('there', 'light', 'autosave', False, my_list)
# # print(hash(default))
#
#
# config[default] = '1' # ключ должен быть хэшируемым


class ITEmployee:
    dept = 'IT'
    def __init__(self, name, id):
        self.name = name
        self.id = id

emp1 = ITEmployee('Alex', 'E101')
emp2 = ITEmployee('Markus', 'E105')

print(emp1.__dict__)
emp1.dept = 'TTT'
emp1.attribut = 16
print(emp1.__dict__)
# print(emp1.dept)
# print(emp2.dept)
#
# emp1.dept = 'Ti'
# print(emp1.dept)
# print(emp2.dept)