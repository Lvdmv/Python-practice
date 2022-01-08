class Circle:

    def __init__(self, radius=1.0, x=0.0, y=0.0):
        self.x = x
        self.y = y
        self.radius = radius

    def area_of_a_circle(self):
        return self.radius ** 2 * 3.14

    def perimeter_of_a_circle(self):
        return self.radius * 2 * 3.14

    def intersects_with(self, two_circle):
        distance = (abs(two_circle.x - self.x)**2 + abs(two_circle.y - self.y)**2)**0.5
        if distance - (two_circle.radius + self.radius) < 0:
            return True
        else:
            return False


radius_circle = int(input('Введите радиус круга: '))
value = Circle(radius_circle)
print(f'Площадь круга равна =  {round(value.area_of_a_circle(), 2)}')
print(f'Периметр круга равен =  {round(value.perimeter_of_a_circle(), 2)}')

k = input("\nВо сколько раз нужно увеличить круг: ")
print(f'Если круг увеличить в {k} раз, то его площадь будет равна {int(k) * value.area_of_a_circle()}')

print('\nПересекается ли круг с новой окружностью?')

cur_x = float(input('Введите x круга: '))
cur_y = float(input('Введите y круга: '))
cur_radius = float(input('Введите r круга: '))
current_circle = Circle(cur_radius, cur_x, cur_y)

new_x = float(input('\nВведите x новой окружности: '))
new_y = float(input('Введите y новой окружности: '))
new_radius = float(input('Введите r новой окружности: '))
new_circle = Circle(new_radius, new_x, new_y)

if current_circle.intersects_with(new_circle):
    print(f'\nНовая окружность пересекается с кругом')
else:
    print(f'\nНовая окружность не пересекается с кругом')
