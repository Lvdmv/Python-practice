class Property:
    def __init__(self, worth):
        self.__worth = worth

    def tax_calculation(self):
        return 1 * self.__worth

    def get_worth(self):
        return self.__worth


class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return (1/1000) * self.get_worth()


class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return (1/200) * self.get_worth()


class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        return (1/500) * self.get_worth()


apartment = Apartment(float(input('Сколько стоит квартира? ')))
car = Car(float(input('Сколько стоит машина? ')))
countryhouse = CountryHouse(float(input('Сколько стоит дача? ')))

amt_money = int(input('Кол-во денег в наличии: '))
coast_property = sum((apartment.tax_calculation(), car.tax_calculation(), countryhouse.tax_calculation()))
print(f'Налог на имущество составит {coast_property}')
if amt_money < coast_property:
    print(f'Не хватает {coast_property - amt_money}, чтобы уплатить налог')

else:
    print(f'Денег на налоги хватает')
