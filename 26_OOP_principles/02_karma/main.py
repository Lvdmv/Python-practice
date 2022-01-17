import random


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


def one_day():
    if random.randint(1, 10) == 1:
        raise random.choice([KillError, DrunkError, CarCrashError, GluttonyError, DepressionError])
    else:
        return random.randint(1, 7)


karma = 0
while karma < 500:
    try:
        bonus_karma = one_day()
        karma += bonus_karma
        print(f'\nДень дал плюс {bonus_karma} очков к карме')
        print(f'Текущее кол-во очков кармы: {karma}\n')
    except KillError:
        print('Умер')
        break
    except DrunkError:
        print('Напился, нет очков к карме')
    except CarCrashError:
        print('Сломалась машина, нет очков к карме')
    except GluttonyError:
        print('Объелся, нет очков к карме')
    except DepressionError:
        print('Депрессия, нет очков к карме')
if karma >= 500:
    print('Просветление достигнуто!')
