def prize_winner(my_dict):
    maxx = max(my_dict.values())
    for i, j in sorted(my_dict.items()):
        if j == maxx:
            return i, my_dict.pop(i)


count_entries = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя): ')
point_dict = dict()
for i_entries in range(1, count_entries + 1):
    print(f'{i_entries} запись: ', end=' ')
    name_points = input().split()
    if not name_points[1] in point_dict:
        point_dict[name_points[1]] = int(name_points[0])
    elif int(name_points[0]) > point_dict[name_points[1]]:
        point_dict[name_points[1]] = int(name_points[0])
print(point_dict)
print('Итоги соревнований: ')
for i_place in range(1, 4):
    name, points = prize_winner(point_dict)
    print(f'{i_place} место. {name} ({points})')


