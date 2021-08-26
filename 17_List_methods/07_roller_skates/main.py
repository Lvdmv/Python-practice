rollers = int(input('Кол-во коньков: '))
roller_list = []
skater_list = []

for i_rol in range(rollers):
    print('Размер', i_rol + 1, 'пары: ', end=' ')
    size_roller = int(input())
    roller_list.append(size_roller)

skaters = int(input('\nКол-во людей: '))
for i_sk in range(skaters):
    print('Размер ноги', i_sk + 1, 'человека: ', end=' ')
    size_skater = int(input())
    skater_list.append(size_skater)
############

count = 0
for i in sorted(skater_list):
    for j in sorted(roller_list):
        if i <= j:
            count += 1
            roller_list.remove(j)
            break
    skater_list.remove(i)


print('\nНаибольшее кол-во людей, которые могут взять ролики: ', count)
