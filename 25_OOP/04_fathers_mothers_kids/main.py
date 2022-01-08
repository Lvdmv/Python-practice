import random


class Parent:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.list_children = []

    def print_info(self):
        print(f'Имя родителя: {self.name}\nВозраст: {self.age}\nДети: {", ".join(self.list_children)}')

    def feed(self, child_name):
        print(f'Родитель {self.name} кормит ребенка {child_name}')
        if not Child(child_name).condition():
            Parent(self.name, self.age).feed(child_name)
        else:
            Child(child_name).is_calm()

    def estimate(self, name):
        print(f'Родитель {self.name} пытается успокоить ребенка {name}')
        if not Child(name).condition():
            print(f'Ребенок {name} по прежнему не спокоен')
            Parent(self.name, self.age).feed(name)


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

    def is_calm(self):
        if not Child(self.name).condition():
            print(f'Состояние ребенка {self.name} - {Child.condition_dict[self.state]}')
            Parent(name_parent, age_parent).estimate(self.name)
        else:
            print(f'Ребенок {self.name} спокоен')


name_parent = input('Имя родителя: ')
age_parent = int(input('Возраст родителя: '))
parents = Parent(name_parent, age_parent)
for i_kid in range(int(input('Введите кол-во детей: '))):
    name_child = input('Имя ребенка: ')
    while True:
        age_child = int(input('Возраст ребенка: '))
        if age_parent - age_child < 16:
            print('Введите корректный возраст ребенка')
        else:
            break
    parents.list_children.append(f'{name_child} возраст: {age_child}')
parents.print_info()

for i_kid in parents.list_children:
    childs = Child(i_kid.split()[0])
    childs.is_calm()
