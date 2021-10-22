def score_key(a):
    return a[1][0]*100000000 - a[1][1]


def filing_name(i_player, index):
    if point_dict[i_player[1]][0] < int(i_player[0]):
        point_dict[i_player[1]] = [int(i_player[0]), index]


count_entries = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя): ')
point_dict = dict()
for i_entries in range(1, count_entries + 1):
    print(f'{i_entries} запись: ', end=' ')
    name_points = input().split()
    if name_points[1] in point_dict:
        filing_name(name_points, i_entries)
    else:
        point_dict[name_points[1]] = [int(name_points[0]), i_entries]

scores = list(point_dict.items())
scores.sort(key=score_key, reverse=True)

print('\nИтоги соревнований: ')
for i_place in range(1, 4):
    print(f'{i_place} место. {scores[i_place -1][0]} ({scores[i_place -1][1][0]})')

