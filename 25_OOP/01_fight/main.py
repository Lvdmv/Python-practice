import random


class Warrior:
    name = 'warrior_name'
    health = 100

    def attack(self, war_object):
        print(f'Бьет {self.name}')
        if war_object.protect():
            war_object.print_health()
            return True
        return False

    def print_health(self):
        print(f'У {self.name}: осталось {self.health} очков здоровья\n')

    def protect(self):
        self.health -= 20
        if self.health > 0:
            return True
        else:
            return False


warrior_1 = Warrior()
warrior_2 = Warrior()
warrior_1.name = 'Воин 1'
warrior_2.name = 'Воин 2'
while True:
    striker = random.choice([warrior_1, warrior_2])
    if striker == warrior_1:
        defend = warrior_2
    else:
        defend = warrior_1
    if not striker.attack(defend):
        print(f'{striker.name} победил')
        break
