class Water:
    def __add__(self, other):
        if type(other) is Air:
            return Storm()
        elif type(other) is Fire:
            return Vapor()
        elif type(other) is Earth:
            return Dirt()
        elif type(other) is Time:
            return Ocean()
        elif type(other) is Magic:
            return Mana()
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
        elif type(other) is Time:
            return Tornado()
        elif type(other) is Magic:
            return Charms()
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
        elif type(other) is Time:
            return Laser()
        elif type(other) is Magic:
            return Spell()
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
        elif type(other) is Time:
            return Mountain()
        elif type(other) is Magic:
            return Gold()
        else:
            return Nothing()


class Time:
    def __add__(self, other):
        if type(other) is Air:
            return Tornado()
        elif type(other) is Fire:
            return Laser()
        elif type(other) is Water:
            return Ocean()
        elif type(other) is Earth:
            return Mountain()
        elif type(other) is Magic:
            return BackInTime()
        else:
            return Nothing()


class Magic:
    def __add__(self, other):
        if type(other) is Air:
            return Charms()
        elif type(other) is Fire:
            return Spell()
        elif type(other) is Water:
            return Mana()
        elif type(other) is Earth:
            return Gold()
        elif type(other) is Time:
            return BackInTime()
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


class Ocean:
    result = 'Океан'


class Mountain:
    result = 'Гора'


class Tornado:
    result = 'Торнадо'


class Laser:
    result = 'Лазерный луч'


class Charms:
    result = 'Чары'


class Spell:
    result = 'Заклинание'


class Mana:
    result = 'Волшебный напиток'


class Gold:
    result = 'Золото'


class BackInTime:
    result = 'Назад во времени'


class Nothing:
    result = None


a = Water()
b = Air()
c = Fire()
d = Earth()
e = Time()
f = Magic()

h = f + f
print(h.result)
