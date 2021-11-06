def sum(*args, my_list=[]):
    summ = 0
    for i_num in args:
        if str(i_num).isdigit():
            my_list.append(i_num)
        else:
            for j_digit in i_num:
                sum(j_digit)
    for i_sum in my_list:
        summ += i_sum
    return summ


print('Ответ:', sum([[1, 2, [3]], [1], 3]))

print('Ответ:', sum(1, 2, 3, 4, 5, my_list=[]))