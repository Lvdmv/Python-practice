class Water:
    def __add__(self, other):
        if type(other) is Air:
            return Storm()
        elif type(other) is Fire:
            return Vapor()
        elif type(other) is Earth:
            return Dirt()
        else:
            return Nothing()


class Air:
    def __add__(self, other):
        if type(other) is Water:
            return Storm()
        elif type(other) is Fire:
            return Lightning()
        elif type(other) is Earth:
            return Dust()
        else:
            return Nothing()


class Fire:
    def __add__(self, other):
        if type(other) is Air:
            return Lightning()
        elif type(other) is Water:
            return Vapor()
        elif type(other) is Earth:
            return Lava()
        else:
            return Nothing()


class Earth:
    def __add__(self, other):
        if type(other) is Air:
            return Dust()
        elif type(other) is Fire:
            return Lava()
        elif type(other) is Water:
            return Dirt()
        else:
            return Nothing()


class Storm:
    result = 'Шторм'


class Vapor:
    result = 'Пар'


class Dirt:
    result = 'Грязь'


class Lava:
    result = 'Лава'


class Dust:
    result = 'Пыль'


class Lightning:
    result = 'Молния'


class Nothing:
    result = None


a = Water()
b = Air()
c = Fire()
d = Earth()

e = a + b
print(e.result)
