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


def error_save(error):
    print(error)
    with open('karma.log', 'a') as errors_file:
        errors_file.write(f'Возникла ошибка {error}\n')


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
        error_save('Умер')
        break
    except DrunkError:
        error_save('Напился, нет очков к карме')
    except CarCrashError:
        error_save('Сломалась машина, нет очков к карме')
    except GluttonyError:
        error_save('Объелся, нет очков к карме')
    except DepressionError:
        error_save('Депрессия, нет очков к карме')
if karma >= 500:
    print('Просветление достигнуто!')
