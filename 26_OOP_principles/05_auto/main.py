import math


class Car:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def __str__(self):
        return f'Машина находится в точке ({self.x}, {self.y})'

    def move(self, distance):
        self.x += math.sin(math.radians(self.angle)) * distance
        self.y += math.cos(math.radians(self.angle)) * distance
        print(f'Машина переехала в точку ({round(self.x, 1)}, {round(self.y, 1)})')

    def turn_around(self, new_angle):
        self.angle += new_angle


class Bus(Car):
    def __init__(self, x, y, angle):
        super().__init__(x, y, angle)
        self.amt_passengers = 0
        self.amt_money = 0

    def come_in(self, passengers):
        self.amt_passengers += passengers
        print(f'Вошло пассажиров {passengers}\nПассажиров в автобусе: {self.amt_passengers}\n')

    def get_out(self, passengers):
        self.amt_passengers -= passengers
        print(f'\nВышло пассажиров {passengers}\nПассажиров в автобусе: {self.amt_passengers}\n')

    def move(self, distance):
        super().move(distance)
        self.amt_money += self.amt_passengers * 1
        print(f'Текущая касса: {self.amt_money}')


bus = Bus(x=0, y=0, angle=45)
bus.come_in(2)
bus.move(5)
bus.come_in(2)
bus.get_out(1)
bus.move(5)
bus.get_out(1)
bus.move(3)
bus.turn_around(30)
bus.move(5)
bus.get_out(1)
