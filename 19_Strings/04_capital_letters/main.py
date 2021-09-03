str_line = input('Введите строку: ').split()

print('Результат: ', (' '.join([i_elem.title() for i_elem in str_line])))
