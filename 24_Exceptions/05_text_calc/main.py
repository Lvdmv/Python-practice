def calc_function(example):
    try:
        if example[1] == '+':
            list_sum.append((int(example[0]) + int(example[2])))
        elif example[1] == '-':
            list_sum.append((int(example[0]) - int(example[2])))
        elif example[1] == '*':
            list_sum.append((int(example[0]) * int(example[2])))
        elif example[1] == '/':
            list_sum.append((int(example[0]) / int(example[2])))
        elif example[1] == '%':
            list_sum.append((int(example[0]) % int(example[2])))
        else:
            raise IndexError
    except IndexError:
        print('Ошибка в написании примера')
    except TypeError:
        print('Операнды должны быть числами')
    except ZeroDivisionError:
        print('На ноль делить нельзя')


list_sum = []
with open('calc.txt', 'r') as calc_file:
    for i_operation in calc_file:
        calc_function(i_operation.split())
print(f'Сумма: {sum(list_sum)}')
