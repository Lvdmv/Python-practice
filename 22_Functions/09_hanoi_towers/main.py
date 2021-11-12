def prints(n, B, C):
    print(f'Переложить диск {n} со стержня номер {B} на стержень номер {C}')
    dict_position[n] = C


def move(n, x, y):
    if n != 0:
        move(n - 1, x, y)
        if (y + n) % 2 != 0:
            if n not in dict_position.keys():
                prints(n, 1, 2)
            else:
                C = dict_position[n]%3 + 1
                prints(n, dict_position[n], C)
        else:
            if n not in dict_position.keys():
                prints(n, 1, 3)
            else:
                C = (dict_position[n]%3 + 1)%3 + 1
                prints(n, dict_position[n], C)
        move(n - 1, x, y)


dict_position = dict()
n = int(input('Введите кол-во дисков: '))
if n % 2 != 0:
    move(n, 1, 3)
else:
    move(n, 1, 2)


