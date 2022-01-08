class Potat:
    states = {0: 'Отсутствует', 1: 'Росток', 2: 'Зеленая', 3: 'Зрелая'}

    def __init__(self, index):
        self.index = index
        self.state = 0

    def grow(self):
        if self.state < 3:
            self.state += 1
        self.print_state()

    def print_state(self):
        print(f'Картошка {self.index} сейчас {Potat.states[self.state]}')

    def is_rape(self):
        if self.state == 3:
            return True
        return False


class PotatoGarden:

    def __init__(self, count):
        self.potatoes = [Potat(i_num) for i_num in range(1, count + 1)]

    def grow_all(self):
        print('Картошка прорастает!')
        for i_potat in self.potatoes:
            i_potat.grow()

    def are_all_ripe(self):
        if not all([i_potat.is_rape() for i_potat in self.potatoes]):
            print('\nКартошка еще не поспела!\n')
            return False
        else:
            print('Вся картошка созрела. Можно собирать\n')
            return True


class Gardener:

    def __init__(self, name):
        self.name = name
        self.harvest_list = []

    def care_of_the_garden(self, garden):
        print(f'Садовник {self.name} ухаживает за грядкой')
        garden.grow_all()

    def harvest(self, count, garden):
        if garden.are_all_ripe():
            self.harvest_list.append(count)
            print(f'Собранно урожая {self.harvest_list}')
        else:
            self.care_of_the_garden(garden)


name_gardener = input('Введите имя садовника: ')
counter = int(input('Сколько посадить картошки: '))
my_gardener = Gardener(name_gardener)
my_garden = PotatoGarden(counter)
while True:
    my_garden = PotatoGarden(counter)
    for _ in range(3):
        my_gardener.harvest(counter, my_garden)
    my_gardener.harvest(counter, my_garden)
    answer = input('\nПосадить еще картошки? да/нет ')
    if answer == 'нет':
        break
    else:
        print(f'\nСадовник {name_gardener} посадил семена')
