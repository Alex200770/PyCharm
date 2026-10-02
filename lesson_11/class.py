class Car:
    color = 'red'
    km = 0

    def show_color(self):
        return self.color

    def add_to_km(self):
        Car.km += 1

mazda = Car()
mazda.add_to_km()
mazda.add_to_km()
print(mazda.km)

BMW = Car()
print(BMW.km)

# my_car = Car()
# print(my_car.km, '\n')
# my_car.add_to_km()
# my_car.add_to_km()
# my_car.add_to_km()
# print(my_car.km)


