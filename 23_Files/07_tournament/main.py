n = input('Введите проходной балл: ')
count_players = int(input('Введите кол-во участников: '))
list_players = []
for _ in range(count_players):
    name_player = input('Введите имя участника и кол-во очков ')
    list_players.append(name_player)
list_info_players = '\n'.join(list_players)

first_tour = open('first_tour.txt', 'w')
first_tour.write(n + '\n')
first_tour.write(list_info_players)
first_tour.close()


def isdigit(data):
    key_name = ''
    value_name = ''
    flag = True
    for i_data in data.split():
        value_name = isdidit_str(i_data)
        if i_data.istitle():
            for i_str in i_data:
                if flag:
                    key_name += i_str
                else:
                    key_name = i_str + '.' + key_name
                    break
            flag = False
    dict_candid[key_name] = value_name


def isdidit_str(number):
    for i_num in number.split():
        if i_num.isdigit():
            return i_num


first_tour = open('first_tour.txt', 'r')
print(f'\nСодержимое файла first_tour.txt:\n{first_tour.read()}')
first_tour.close()

first_tour = open('first_tour.txt', 'r')
new_line = 1
dict_candid = dict()
passing_score = ''
for i_player in first_tour:
    if new_line == 1:
        for i in i_player:
            if i.isdigit():
                passing_score += i
    elif int(isdidit_str(i_player)) > int(passing_score):
        isdigit(i_player)
    new_line += 1
first_tour.close()

list_candid = []
for i_num, i_suc_candid in enumerate(sorted(dict_candid, key=dict_candid.get, reverse=True)):
    list_candid.append(f'{i_num+1}) {i_suc_candid} {"".join(dict_candid[i_suc_candid])}')
new_list_candid = '\n'.join(list_candid)

second_tour = open('second_tour.txt', 'w')
second_tour.write(str(len(list_candid)) + '\n')
second_tour.write(new_list_candid)
second_tour.close()

second_tour = open('second_tour.txt', 'r')
print(f'\nСодержимое файла second_tour.txt: \n{second_tour.read()}')
second_tour.close()
