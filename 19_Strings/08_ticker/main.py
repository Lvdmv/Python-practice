def reverse_str(my_list, my_list2):
    count = 0
    for _ in enumerate(my_list):
        if my_list != my_list2:
            my_list.append(my_list[0])
            my_list.remove(my_list[0])
            count += 1
        else:
            return count
    return False


fst_str = input('Первая строка: ')
snd_str = input('Вторая строка: ')
if reverse_str(list(fst_str), list(snd_str)):
    print('Первая строка получается из второй со сдвигом', reverse_str(list(fst_str), list(snd_str)))
else:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')






