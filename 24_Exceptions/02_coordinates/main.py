import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    if y == 0:
        raise ZeroDivisionError('Ошибка в первой функции')
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    if x == 0:
        raise ZeroDivisionError('Ошибка во второй функции')
    return y / x


try:
    with open('coordinates.txt', 'r') as file:
        for line in file:
            nums_list = line.split()
            res1 = f(int(nums_list[0]), int(nums_list[1]))
            res2 = f2(int(nums_list[0]), int(nums_list[1]))
            number = random.randint(0, 100)
            my_list = sorted([res1, res2, number])
            with open('result.txt', 'a') as file_2:
                for i_num in my_list:
                    file_2.write(str(round(i_num, 3)))
                    file_2.write(' ')
                file_2.write('\n')
except ZeroDivisionError:
    print('На ноль делить нельзя')
    raise
