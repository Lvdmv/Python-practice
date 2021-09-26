def simmetrical_str(my_str):
    new_list = dict()
    for i_dict in my_str:
        if not i_dict in new_list:
            new_list[i_dict] = 1
        else:
            new_list[i_dict] += 1

    if len({i_num for i_num in new_list.keys() if new_list[i_num] % 2 != 0}) <= 1:
        return True
    else:
        return False


new_str = input('Введите строку: ')
if simmetrical_str(new_str):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')
