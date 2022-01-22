class Person:
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def __str__(self):
        return f'Имя: {self.__name}\nФамилия: {self.__surname}\nВозраст: {self.__age}'

    def salary_calculation(self):
        pass


class Employee(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)


class Manager(Employee):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname, age)
        self.salary = salary

    def salary_calculation(self):
        print(f'Должность: Менеджер\n{super().__str__()}')
        print(f'Его зарплата: {self.salary}\n')


class Agent(Employee):
    def __init__(self, name, surname, age, volume_sales):
        super().__init__(name, surname, age)
        self.volume_sales = volume_sales

    def salary_calculation(self):
        print(f'Должность: Агент\n{super().__str__()}')
        print(f'Его зарплата: {5000 + self.volume_sales*0.05}\n')


class Worker(Employee):
    def __init__(self, name, surname, age, hours_worked):
        super().__init__(name, surname, age)
        self.hours_worked = hours_worked

    def salary_calculation(self):
        print(f'Должность: Рабочий\n{super().__str__()}')
        print(f'Его зарплата: {100 * self.hours_worked}')


manager = Manager(name='Петр', surname='Петров', age=18, salary=50000)
manager.salary_calculation()
agent = Agent(name='Вася', surname='Иванов', age=23, volume_sales=500000)
agent.salary_calculation()
worker = Worker(name='Иван', surname='Васильев', age=11, hours_worked=1200)
worker.salary_calculation()
