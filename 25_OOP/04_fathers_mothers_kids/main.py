import random


class Parent:

    def __init__(self, name):
        self.name = name
        self.age = ''
        self.list_children = []

    def print_info(self):
        print(f'Имя родителя: {self.name}\nВозраст: {self.age}\nДети: {", ".join(self.list_children)}')

    def feed(self, child):
        print(f'Родитель {self.name} кормит ребенка {child.name}')
        if not child.is_calm():
            self.feed(child)

    def estimate(self, child):
        print(f'Родитель {self.name} пытается успокоить ребенка {child.name}')
        if not child.is_calm():
            self.feed(child)


class Child:
    condition_dict = {0: 'спокойствие', 1: 'голод'}

    def __init__(self, name):
        self.name = name
        self.age = 0
        self.state = 1

    def condition(self):
        self.state = random.randint(0, 1)
        if self.state == 0:
            return True
        else:
            return False

    def is_calm(self):
        if not self.condition():
            print(f'Состояние ребенка {self.name} - {Child.condition_dict[self.state]}')
            return False
        else:
            self.calm()
            return True

    def calm(self):
        print(f'Ребенок {self.name} спокоен')


name_parent = input('Имя родителя: ')
parent = Parent(name_parent)
parent.age = int(input('Возраст родителя: '))

for i_kid in range(int(input('Введите кол-во детей: '))):
    name_child = input('Имя ребенка: ')
    while True:
        age_child = int(input('Возраст ребенка: '))
        if parent.age - age_child < 16:
            print('Введите корректный возраст ребенка')
        else:
            break
    parent.list_children.append(name_child)
parent.print_info()

for i_kid in parent.list_children:
    childs = Child(i_kid)
    if not childs.is_calm():
        parent.estimate(childs)
