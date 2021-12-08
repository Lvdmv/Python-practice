import random


class Student:
    def __init__(self, name, num_group):
        self.name = name
        self.num_group = num_group
        self.progress = [random.randint(1, 5) for _ in range(5)]

    def record_in_a_dict(self):
        dict_stud[self.name, self.num_group] = sum(self.progress)


dict_stud = dict()
for _ in range(10):
    student = Student(input('Введите ФИ: '), int(input('Введите номер гр: ')))
    student.record_in_a_dict()

for i in sorted(dict_stud, key=dict_stud.get, reverse=True):
    print(f'Студент {i[0]}, группа {i[1]}, средний балл успеваемости: {dict_stud[i]}')
