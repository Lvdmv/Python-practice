import random


def score(new_object):
    average_score = round(sum(new_object.progress)/(len(new_object.progress)), 1)
    return average_score


class Student:

    def __init__(self, name):
        self.name = name
        self.num_group = 0
        self.progress = 0


list_students = []

for _ in range(10):
    student = Student(input('Введите ФИ: '))
    list_students.append(student)
    student.num_group = int(input('Введите номер гр: '))
    student.progress = [random.randint(1, 5) for _ in range(5)]

for i in sorted(list_students, key=score, reverse=True):
    print(f'Студент {i.name}, группа {i.num_group}, средний балл успеваемости: {score(i)}')
