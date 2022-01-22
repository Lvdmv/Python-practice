import random


class KillHunger(Exception):
    pass


class KillDepression(Exception):
    pass


class House:
    def __init__(self):
        self.cash = 100
        self.in_fridge = 50
        self.cat_bowl = 30
        self.garbage = 0

    def __str__(self):
        return f'Деньги в тумбочке {self.cash}'

    def act(self):
        self.garbage += 5

    def much_dirt(self):
        if self.garbage >= 90:
            return True
        return False

    def is_food(self):
        if self.in_fridge > 0:
            if self.cat_bowl > 0:
                return True
        return False


def eaten_food(amount):
    Person.amt_eaten_food += amount


class Person:
    amt_eaten_food = 0

    def __init__(self, name, house):
        self.__name = name
        self.satiety_level = 30
        self.happiness_level = 100
        self.house = house

    def __str__(self):
        return f'Имя: {self.__name}\nСытость: {self.satiety_level}'

    def act(self):
        if self.house.much_dirt():
            self.happiness_level -= 10

    def get_name(self):
        return self.__name

    def eat(self):
        print(f'{self.__name} ест')
        need_food = 30 - self.satiety_level
        if self.house.in_fridge < need_food:
            need_food = self.house.in_fridge
        self.satiety_level += need_food
        eaten_food(need_food)
        self.house.in_fridge -= need_food

    def hungry(self):
        self.satiety_level -= 10

    def pet_the_cat(self):
        print(f'{self.__name} гладит кота')
        self.happiness_level += 5
        self.hungry()

    def is_alive(self):
        if self.satiety_level >= 0:
            if self.happiness_level > 10:
                return True
            else:
                print(f'{self.get_name()}', end='')
                raise KillDepression
        else:
            print(f'{self.get_name()}', end='')
            raise KillHunger


class Husband(Person):
    amt_money_earned = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def act(self):
        super().act()
        if self.is_alive():
            print(super().__str__())
            print(f'Счастье: {self.happiness_level}')
            if self.satiety_level < 11:
                self.eat()
            elif self.happiness_level < 50:
                self.improve_mood()
            elif self.house.cash < 300:
                self.go_to_work()
            print()

    def go_to_work(self):
        print(f'{self.get_name()} идет на работу')
        self.house.cash += 290
        Husband.amt_money_earned += 150
        self.hungry()

    def play(self):
        self.happiness_level += 20
        self.hungry()

    def improve_mood(self):
        if self.happiness_level <= 80:
            self.play()
        else:
            self.pet_the_cat()


class Wife(Person):
    amt_fur_coat = 0

    def __init__(self, name, house):
        super().__init__(name, house)

    def act(self):
        super().act()
        if self.is_alive():
            print(super().__str__())
            print(f'Счастье: {self.happiness_level}')
            if self.satiety_level < 11:
                self.eat()
            elif self.house.much_dirt():
                self.cleaning()
            elif self.happiness_level < 50:
                self.improve_mood()
            elif not self.house.is_food():
                self.buy_eat()
                self.buy_cat_eat()
            print()

    def buy_eat(self):
        if self.is_alive():
            print(f'{self.get_name()} покупает еду')
            add_food = 50 - self.house.in_fridge
            if add_food > self.house.cash:
                print(f'{self.get_name()} купила еды на последние деньги')
                add_food = self.house.cash
            self.house.in_fridge += add_food
            self.house.cash -= add_food
            self.hungry()

    def buy_cat_eat(self):
        print(f'{self.get_name()} покупает кошачью еду')
        add_food = 30 - self.house.cat_bowl
        if add_food > self.house.cash:
            print(f'{self.get_name()} купила кошачьей еды на последние деньги')
            add_food = self.house.cash
        self.house.cat_bowl += add_food
        self.house.cash -= add_food
        self.hungry()

    def improve_mood(self):
        if self.house.cash >= 350:
            print(f'{self.get_name()} покупает шубу')
            self.happiness_level += 60
            self.house.cash -= 350
            self.hungry()
            Wife.amt_fur_coat += 1
        else:
            print(f'{self.get_name()} хотела шубу, но денег нет')
            self.pet_the_cat()

    def cleaning(self):
        print(f'{self.get_name()} убирается дома')
        if self.house.garbage <= 100:
            self.house.garbage -= self.house.garbage
        else:
            self.house.garbage -= 100
        self.hungry()


class Child(Person):
    def __init__(self, name, house):
        super().__init__(name, house)

    def act(self):
        super().act()
        if self.is_alive():
            print(super().__str__())
            print(f'Счастье: {self.happiness_level}')
            if self.satiety_level < 11:
                self.eat()
            elif self.happiness_level < 100:
                self.improve_mood()
            print()

    def play(self):
        self.happiness_level += 20
        self.hungry()

    def improve_mood(self):
        if self.happiness_level <= 90:
            self.play()
        else:
            self.pet_the_cat()


class Cat(Person):
    def __init__(self, name, house):
        super().__init__(name, house)

    def act(self):
        if self.is_alive():
            print(super().__str__())
            if self.satiety_level < 11:
                self.eat()
            else:
                random.choice([self.sleep, self.destroy])()
        print()

    def eat(self):
        print(f'{self.get_name()} ест')
        need_food = ((30 - self.satiety_level) // 2) * 2
        if self.house.cat_bowl < need_food:
            need_food = self.house.cat_bowl * 2
        if need_food > 20:
            need_food = 20
        eaten_food(need_food)
        self.satiety_level += need_food
        self.house.cat_bowl -= need_food // 2

    def destroy(self):
        print(f'{self.get_name()} дерет обои')
        self.house.garbage += 5
        self.hungry()

    def sleep(self):
        print(f'{self.get_name()} спит')
        self.hungry()


our_house = House()
husband = Husband('Игорь', our_house)
wife = Wife('Тамара', our_house)
child = Child('Петя', our_house)
cat_fst = Cat('Мурка', our_house)
cat_scd = Cat('Мурзик', our_house)
cat_tre = Cat('Рыжий', our_house)


list_of_livers = [husband, wife, child, cat_fst, cat_scd, cat_tre, our_house]

try:
    for i in range(365):
        print(f'\nДень {i + 1}')
        for i_person in list_of_livers:
            i_person.act()
except KillHunger:
    print(' - смерть по причине голода')
except KillDepression:
    print(' - смерть от несчастья')
else:
    print('\nСемья прожила год.')
    print(f'За это время семья смогла:')
    print(f'\nЗаработано денег: {husband.amt_money_earned}')
    print(f'Съедено еды: {Person.amt_eaten_food}')
    print(f'Куплено шуб: {wife.amt_fur_coat}')
