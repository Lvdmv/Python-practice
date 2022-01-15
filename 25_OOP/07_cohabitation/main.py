import random


class Person:

    def __init__(self, name, house):
        self.name = name
        self.satiety_level = 50
        self.house = house

    def eating(self):
        self.satiety_level += 1
        self.house.refrigerator -= 1

    def work(self):
        self.house.nightstand_with_money += 1
        self.satiety_level -= 1

    def play(self):
        self.satiety_level -= 1

    def go_for_food(self):
        if self.house.nightstand_with_money > 0:
            self.house.refrigerator += 1
        self.house.nightstand_with_money -= 1

    def live_one_day(self):
        if not self.house.is_have:
            return False
        else:
            action = random.randint(1, 6)
            if self.satiety_level < 20:
                self.eating()
            elif self.house.refrigerator < 10:
                self.go_for_food()
            elif self.house.nightstand_with_money < 50:
                self.work()
            elif action == 1:
                self.work()
            elif action == 2:
                self.eating()
            else:
                self.play()
        if self.satiety_level < 0:
            print(f'Сытость {person.name} меньше нуля, он умер')
            self.house.is_have = False
        else:
            return True


class House:
    is_have = True
    refrigerator = 50
    nightstand_with_money = 0


list_person = []

for _ in range(2):
    list_person.append(Person(input('Введите имя: '), House()))
out_list = []
for _ in range(365):
    if not len(out_list) == len(list_person):
        for person in list_person:
            if person.live_one_day():
                print(f'{person.name} прожил еще один день')
            elif person not in out_list:
                out_list.append(person)
    else:
        break
for tenant in list_person:
    if tenant.house.is_have:
        print(f'{tenant.name} дожил до конца года')
