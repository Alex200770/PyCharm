class Bus:
    def __init__(self, max_seats, max_speed):
        self.max_speed = max_speed
        self.max_seats = max_seats
        self.speed = 0
        self.passengers = []
        self.seats_all = {i: None for i in range(1, max_seats + 1)}
    def board(self, second_name):
        if len(self.passengers) >= self.max_seats:
            print(f'Для вас {second_name} мест нет')
            return
        for seat in self.seats_all:
            if self.seats_all[seat] is None:
                self.seats_all[seat] = second_name
                break
            self.passengers.append(seat)
            print(f'{second_name} сел')
    def disembark(self, second_name):
        if second_name not in self.passengers:
            print(f'{second_name} не в автобусе')
            return
        self.passengers.remove(second_name)
        for seat in self.seats_all:
            if self.seats_all[seat] is None:
                self.seats_all[seat] = None
                break
            print(f'{second_name} вышел')

    def change_speed(self, delta):
        self.speed = self.speed + delta
        if self.speed < 0:
            self.speed = 0
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        print(f"Скорость: {self.speed}")

    def __contains__(self, name):
        return name in self.passengers

    def __iadd__(self, name):
        self.board(name)
        return self

    def __isub__(self, name):
        self.disembark(name)
        return self

bus = Bus(3, 60)

bus += "Иванов"
bus += "Петров"
bus += "Сидоров"
bus += "Кузнецов"   # не сядет

print("Иванов тут?", "Иванов" in bus)   # True

bus -= "Петров"
print("Петров тут?", "Петров" in bus)   # False

bus.change_speed(40)
bus.change_speed(30)
bus.change_speed(-100)

print("Места:", bus.seats_all)
print("Пассажиры:", bus.passengers)