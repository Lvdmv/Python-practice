import random


class Person:
    amt_eaten_food = 0

    def __init__(self, name, house):
        self.__name = name
        self.satiety_level = 30
        self.happiness_level = 100
        self.house = house

    def eat(self):
        print(f'{self.__name} ест')
        amt_food = 30 - self.satiety_level
        if amt_food >= self.house.food_in_fridge:
            amt_food = self.house.food_in_fridge
        self.satiety_level += amt_food
        self.house.food_in_fridge -= amt_food
        Person.amt_eaten_food += amt_food

    def get_name(self):
        return self.__name

    def pet_the_cat(self):
        print(f'{self.__name} гладит кота')
        self.happiness_level += 5
        self.satiety_level -= 10

    def is_life(self):
        if self.satiety_level < 0:
            return False
        elif self.happiness_level < 10:
            return False
        else:
            return True


class Cat(Person):
    def __init__(self, name, house):
        super().__init__(name, house)

    def eat(self):
        print(f'{self.get_name()} ест')
        amt_food = 30 - self.satiety_level
        if amt_food >= self.house.cats_food:
            amt_food = self.house.cats_food
        self.satiety_level += amt_food
        self.house.cats_food -= amt_food
        Person.amt_eaten_food += amt_food

    def sleep(self):
        print(f'{self.get_name()} спит')
        self.satiety_level -= 10

    def fights_wallpaper(self):
        print(f'{self.get_name()} дерет обои')
        self.house.amt_dirt += 5
        self.satiety_level -= 10


class Husband(Person):
    amt_money_earned = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def play(self):
        print(f'{self.get_name()} играет в компьютер')
        self.happiness_level += 20
        self.satiety_level -= 10

    def go_to_work(self):
        print(f'{self.get_name()} идет на работу')
        self.house.money_in_nightstand += 150
        self.amt_money_earned += 150
        self.satiety_level -= 10


class Wife(Person):
    amt_fur_coat = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def buy_food(self):
        print(f'{self.get_name()} покупает еду')
        self.satiety_level -= 10
        if self.house.money_in_nightstand >= 140:
            self.house.money_in_nightstand -= 140
            self.house.food_in_fridge = 70
            self.house.cats_food = 70
            print(f'{self.get_name()} сходила в магазин. Денег ок')
            return True
        elif self.house.money_in_nightstand >= 70:
            self.house.money_in_nightstand = 0
            self.house.food_in_fridge = 70
            self.house.cats_food += self.house.money_in_nightstand - 70
            self.house.money_in_nightstand = 0
        else:
            self.house.money_in_nightstand = 0
            self.house.food_in_fridge = self.house.money_in_nightstand
        print(f'{self.get_name()} сходила в магазин. Мало денег!')

    def buy_fur_coat(self):
        print(f'{self.get_name()} хочет купить шубу')
        print(f'Денег на момент - {self.house.money_in_nightstand}')
        if self.house.money_in_nightstand >= 350:
            self.house.money_in_nightstand -= 350
            self.happiness_level += 60
            self.amt_fur_coat += 1
            print(f'{self.get_name()} покупает шубу')
            return True
        else:
            print('На шубу денег не хватает, поэтому')
        self.satiety_level -= 10

    def clean_house(self):
        print(f'{self.get_name()} убирается дома')
        if self.house.amt_dirt > 100:
            self.house.amt_dirt -= 100
        else:
            self.house.amt_dirt = 0
        self.satiety_level -= 10


class Child(Person):
    def __init__(self, name, house):
        super().__init__(name, house)


class House:
    money_in_nightstand = 100
    food_in_fridge = 50
    cats_food = 30
    amt_dirt = 0


def lived_one_day(member):
    if member.satiety_level < 11:
        member.eat()
    elif isinstance(member, Cat):
        random.choice((member.sleep, member.fights_wallpaper))()
    elif isinstance(member, Husband):
        if my_house.money_in_nightstand < 200:
            member.go_to_work()
    elif member.happiness_level < 95:
        if isinstance(member, Husband):
            husband.play()
        elif not wife.buy_fur_coat():
            wife.pet_the_cat()
            husband.go_to_work()
    elif isinstance(member, Wife):
        if my_house.food_in_fridge < 50:
            wife.buy_food()
        elif my_house.cats_food < 30:
            wife.buy_food()
        else:
            wife.clean_house()
    elif member.happiness_level in range(95, 100):
        member.pet_the_cat()
    member.satiety_level -= 1
    if not member.is_life():
        return False
    else:
        return True


my_house = House()
husband = Husband(input('Имя мужа: '), my_house)
wife = Wife(input('Имя жены: '), my_house)
child = Child(input('Имя ребенка: '), my_house)
cat_fst = Cat(input('Имя первого кота: '), my_house)
cat_scd = Cat(input('Имя второго кота: '), my_house)
cat_tre = Cat(input('Имя третьего кота: '), my_house)

list_famile = [husband, wife, child, cat_fst, cat_scd, cat_tre]

for _ in range(365):
    if not [i_mem for i_mem in [husband, wife, child, cat_fst, cat_scd, cat_tre] if not i_mem.is_life()]:
        my_house.amt_dirt += 5
        if my_house.amt_dirt >= 90:
            husband.happiness_level -= 10
            wife.happiness_level -= 10
        print('Кол-во пыли:', my_house.amt_dirt)
        for i_member in list_famile:
            if not lived_one_day(i_member):
                break
    else:
        break


if not [i_mem for i_mem in [husband, wife, child, cat_fst, cat_scd, cat_tre] if not i_mem.is_life()]:
    print('Семья прожила год.\n')
    print(f'За это время семья смогла:')
    print(f'\nЗаработано денег: {husband.amt_money_earned}')
    print(f'Съедено еды: {Person.amt_eaten_food}')
    print(f'Куплено шуб: {wife.amt_fur_coat}')
else:
    print('Умер член семьи')
