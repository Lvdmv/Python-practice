n = int(input('Введите кол-во символов: '))
list = [(1 if i_elem % 2 == 0 else i_elem % 5) for i_elem in range(n)]
print('Результат: ', list)
