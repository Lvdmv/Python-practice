import random


class Person:

    def __init__(self, name):
        self.name = name
        self.satiety_level = 50
        self.have_a_house = True

    def eating(self, fill):
        if fill.refrigerator > 0:
            self.satiety_level += 1
        fill.refrigerator -= 1

    def work(self, fill):
        fill.nightstand_with_money += 1
        self.satiety_level -= 1

    def play(self):
        self.satiety_level -= 1

    def go_for_food(self, fill):
        if self.have_a_house:
            if fill.nightstand_with_money > 0:
                fill.refrigerator += 1
            fill.nightstand_with_money -= 1


class House:

    def __init__(self, name):
        self.name = name
        self.refrigerator = 50
        self.nightstand_with_money = 0


def year_of_life(person):
    for _ in range(365):
        if new_name.satiety_level < 0:
            print(f'Сытость {person} меньше нуля, он умер')
            return False
        action = random.randint(1, 6)
        if new_name.satiety_level < 20:
            new_name.eating(fullness)
        elif fullness.refrigerator < 10:
            new_name.go_for_food(fullness)
        elif fullness.nightstand_with_money < 50:
            new_name.work(fullness)
        elif action == 1:
            new_name.work(fullness)
        elif action == 2:
            new_name.eating(fullness)
        else:
            new_name.play()
    return True


list_person = []
for _ in range(2):
    list_person.append(input('Введите имя: '))
for my_name in list_person:
    fullness = House(my_name)
    satiety = Person(my_name)
    new_name = Person(my_name)
    if year_of_life(my_name):
        print(f'{my_name} дожил до конца года')
