def height(my_key, my_dict):
    for i in my_dict:
        for i_key in i.keys():
            if my_key == i_key:
                return i[i_key] + 1


amt_person = int(input('Введите кол-во человек: '))
pair_dict = {'Peter_I': {'Peter_I': 0}}
for i_person in range(amt_person - 1):
    print(i_person + 1, 'пара: ', end='')
    pair = input()
    if not pair.split()[1] in pair_dict.keys():
        pair_dict[pair.split()[1]] = {pair.split()[0]: height(pair.split()[1], pair_dict.values())}

    else:
        pair_dict[pair.split()[1]][pair.split()[0]] = height(pair.split()[1], pair_dict.values())
print(pair_dict)
print()
print('"Высота" каждого члена семьи: ')
for i_pair in sorted({i: j[i] for j in pair_dict.values() for i in j}.keys()):
    print(i_pair, {i: j[i] for j in pair_dict.values() for i in j}[i_pair])


