class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Vapor()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Time):
            return Ocean()
        elif isinstance(other, Magic):
            return Mana()
        else:
            return Nothing()


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Earth):
            return Dust()
        elif isinstance(other, Time):
            return Tornado()
        elif isinstance(other, Magic):
            return Charms()
        else:
            return Nothing()


class Fire:
    def __add__(self, other):
        if isinstance(other, Air):
            return Lightning()
        elif isinstance(other, Water):
            return Vapor()
        elif isinstance(other, Earth):
            return Lava()
        elif isinstance(other, Time):
            return Laser()
        elif isinstance(other, Magic):
            return Spell()
        else:
            return Nothing()


class Earth:
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        elif isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Time):
            return Mountain()
        elif isinstance(other, Magic):
            return Gold()
        else:
            return Nothing()


class Time:
    def __add__(self, other):
        if isinstance(other, Air):
            return Tornado()
        elif isinstance(other, Fire):
            return Laser()
        elif isinstance(other, Water):
            return Ocean()
        elif isinstance(other, Earth):
            return Mountain()
        elif isinstance(other, Magic):
            return BackInTime()
        else:
            return Nothing()


class Magic:
    def __add__(self, other):
        if isinstance(other, Air):
            return Charms()
        elif isinstance(other, Fire):
            return Spell()
        elif isinstance(other, Water):
            return Mana()
        elif isinstance(other, Earth):
            return Gold()
        elif isinstance(other, Time):
            return BackInTime()
        else:
            return Nothing()


class Storm:
    result = '??????????'


class Vapor:
    result = '??????'


class Dirt:
    result = '??????????'


class Lava:
    result = '????????'


class Dust:
    result = '????????'


class Lightning:
    result = '????????????'


class Ocean:
    result = '??????????'


class Mountain:
    result = '????????'


class Tornado:
    result = '??????????????'


class Laser:
    result = '???????????????? ??????'


class Charms:
    result = '????????'


class Spell:
    result = '????????????????????'


class Mana:
    result = '?????????????????? ??????????????'


class Gold:
    result = '????????????'


class BackInTime:
    result = '?????????? ???? ??????????????'


class Nothing:
    result = None


a = Water()
b = Air()
c = Fire()
d = Earth()
e = Time()
f = Magic()

h = f + a
print(h.result)
