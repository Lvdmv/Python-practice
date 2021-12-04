def right_data(data):
    with open('registrations_good.log', 'a', encoding='utf-8') as good_file:
        good_file.write(data)


def wrong_data(data):
    with open('registrations_bad.log', 'a', encoding='utf-8') as bad_file:
        bad_file.write(data)


def error_function(data):
    try:
        if len(data) != 3:
            raise ValueError
        if not data[0].isalpha():
            raise NameError
        if '@' not in data[1] and '.' not in data[1]:
            raise SyntaxError
        if 10 <= int(data[2]) >= 99:
            raise ValueError
    except ValueError:
        print('Не присутствуют все три поля')
    except NameError:
        print('Поле имени содержит НЕ только буквы')
    except SyntaxError:
        print('Поле «Имейл» НЕ содержит @ и .(точку)')
    else:
        return True


with open('registrations.txt', 'r', encoding='utf-8') as reg_file:
    for i_info in reg_file:
        info = i_info.split()
        if error_function(info):
            right_data(i_info)
        else:
            wrong_data(i_info)
