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
        answer = input(f'Обнаружена ошибка в строке {" ".join(example)} исправить? да/нет ')
        if answer == 'да':
            new_exam = input('Введите исправленную строку: ')
            calc_function(new_exam.split())
    else:
        return True


list_sum = []
with open('calc.txt', 'r') as calc_file:
    for i_operation in calc_file:
        calc_function(i_operation.split())
print(f'Сумма: {sum(list_sum)}')
