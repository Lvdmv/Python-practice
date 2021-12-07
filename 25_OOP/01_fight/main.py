import random


class Warriors:
    health = [100, 100]

    def __init__(self, index):
        self.index = index

    def take_a_blow(self):
        Warriors.health[self.index] -= 20
        self.print_health()
        if Warriors.health[self.index] > 0:
            return True
        else:
            return False

    def print_health(self):
        print(f'У воина {self.index + 1}: осталось {Warriors.health[self.index]} очков здоровья\n')

    def have_a_health_reserve(self):
        if not Warriors(self.index).take_a_blow():
            return False
        else:
            return True


while True:
    striker_warrior = random.randint(1, 2)
    print(f'Бьет воин {striker_warrior}')
    bruised_warrior = Warriors((striker_warrior % 2 + 1) - 1)
    if not bruised_warrior.have_a_health_reserve():
        print(f'Воин {striker_warrior} победил')
        break
