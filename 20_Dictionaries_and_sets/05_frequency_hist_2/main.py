def inverted_dict(my_dict, i):
    return [i_key for i_key in my_dict.keys() if my_dict[i_key] == i]


text = input('Введите текст: ')
print('Оригинальный словарь частот:', end = '\n')
sym_str = dict()
for i_let in text:
    if i_let in sym_str:
        sym_str[i_let] += 1
    else:
        sym_str[i_let] = 1
for i_num in sorted(sym_str.keys()):
    print(i_num, ':', sym_str[i_num])
print('\nИнвертированный словарь частот:\n')
for i_word in set(sym_str.values()):
    print(i_word, ':', inverted_dict(sym_str, i_word))
