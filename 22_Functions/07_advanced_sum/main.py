def sum(*args):
    summ = 0
    for i_num in args:
        if str(i_num).isdigit():
            summ += i_num
        else:
            for i_elem in i_num:
                summ += sum(i_elem)
    return summ


print('Ответ:', sum([[1, 2, [3]], [1], 3]))
print('Ответ:', sum(1, 2, 3, 4, 5))
