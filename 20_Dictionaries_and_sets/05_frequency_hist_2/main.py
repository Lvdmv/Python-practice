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
    print(i_word, ':', [i_key for i_key in sym_str.keys() if sym_str[i_key] == i_word])
    print()
