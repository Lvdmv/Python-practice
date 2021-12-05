def error_save(line):
    with open('people.txt', 'w') as errors_file:
        errors_file.write(f'В строке {line} возникла ошибка TypeError')


sym_sum = 0
num_line = 1
try:
    with open('people.txt', 'r') as people_file:
        for i_line in people_file:
            lenght = len(i_line)
            if i_line.endswith('\n'):
                lenght -= 1
            if lenght < 3:
                raise TypeError
            sym_sum += lenght
            num_line += 1
except FileNotFoundError:
    print('Файл не найден')
except TypeError:
    print('Кол-во букв в имени пользователя меньше 3-х')
    error_save(num_line)
finally:
    print('Общее кол-во символов:', sym_sum)
