def if_elem(sim, my_list2):
    border = 0
    if sim in my_list2:
        border = my_list2.index(sim)
        my_list2.remove(sim)
    return border

def new_tuple(my_tuple, simbol):
    my_list = list(my_tuple)
    fst_list = if_elem(simbol, my_list)
    end_list = if_elem(simbol, my_list)
    return tuple(my_list[fst_list:end_list])


fst_tuple = (1, 2, 'a', 3, 2, 1, 'a')
elem = input('Введите элемент: ')

if elem.isdigit():
    print(new_tuple(fst_tuple, int(elem)))
else:
    print(new_tuple(fst_tuple, elem))


