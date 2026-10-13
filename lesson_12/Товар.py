class Product:
    # описание из чего состоит товар: имя, магазин, цена
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    @property
    def name(self):
        return self.__name
    @property
    def store(self):
        return self.__store
    @property
    def price(self):
        return self.__price
    def __add__(self, other):
        if isinstance(other, Product):
            new_name = f'{self.__name} + {other.__name}'
            new_store = self.__store
            new_price = f'{self.__price + other.__price}'
            return Product(new_name, new_store, new_price)
        return TypeError('Товар складывается с товаром, а цена с ценой, вы что-то напутали')
    def __repr__(self):
        return f"Товар('{self.__name}', магазин: '{self.__store}', цена: {self.__price} руб.)"

class Storehouse:
    def __init__(self):
        self.__products = []
    def add_product(self, product):
        self.__products.append(product)
    def __getitem__(self, index):
        return self.__products[index]
    def find_product_by_name(self, name):
        for product in self.__products:
            if product.name == name:
                return product
        return None
    def name_sort(self):
        self.__products.sort(key=lambda p: p.name)
    def store_sort(self):
        self.__products.sort(key=lambda p: p.store)
    def price_sort(self):
        self.__products.sort(key=lambda p: p.price)
    def print_all(self):
        for p in self.__products:
            print(p)

stuff1 = Product('Яйца', 'Магнит', 2.3)
stuff2 = Product('Молоко', 'Евроопт', 3)
stuff3 = Product('Хлеб', 'Грошик', 1.2)

storehouse = Storehouse()
storehouse.add_product(stuff1)
storehouse.add_product(stuff2)
storehouse.add_product(stuff3)

print('       Смотрим по индексу содержемое склада')
print(storehouse[0])
print(storehouse[1])
print(storehouse[2])
print()

print('Поиск товара по имени for example Молоко')
print(storehouse.find_product_by_name('Молоко'))
print()

print('Сортировка по названию магазина')
storehouse.store_sort()
storehouse.print_all()
print()

print('Сортировка по цене')
storehouse.price_sort()
storehouse.print_all()
print()

print('Сортировка по названию товара')
storehouse.name_sort()
storehouse.print_all()
print()

print('Сложение товаров')
new_product = stuff1 + stuff2
print(new_product)




#     def __repr__(self):
#         return f"Товар('{self.__name}', магазин: '{self.__store}', цена: {self.__price} руб.)"
#
# t1 = Product('Хлеб', 'fec', '34')
# print(t1)