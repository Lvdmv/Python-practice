def countSkaters(my_list_1, my_list_2, i, j):
    skaters = 0
    for i_sk in range(1, my_list_1.count(my_list_1[j]) + 1):
        if i_sk == my_list_1.count(my_list_1[i]):
            if i_sk > my_list_2.count(my_list_2[i]):
                skaters += my_list_2.count(my_list_2[i])
            else:
                skaters += my_list_1.count(my_list_1[j])
    return skaters

def delIndex(my_list, j):
    size = my_list[j]
    for _ in range(my_list.count(size)):
        my_list.remove(size)


skates_amt = int(input('Кол-во коньков: '))
skates_list = []
skaters_list = []

for i_skates_amt in range(skates_amt):
    print('Размер ', i_skates_amt + 1, ' пары: ', end = ' ')
    skates = int(input())
    skates_list.append(skates)
skates_men = int(input('\nКол-во людей: '))

for i_skates_amt in range(skates_men):
    print('Размер ноги ', i_skates_amt + 1, ' человека: ', end = ' ')
    skater = int(input())
    skaters_list.append(skater)

count = 0
i = 0
while len(skaters_list) != 0:
    flag = True
    for num in range(len(skates_list)):
        if skaters_list[i] == skates_list[num]:
            flag = False
            if skaters_list.count(skaters_list[i]) == skates_list.count(skates_list[num]):
                count += skaters_list.count(skaters_list[i])
                delIndex(skates_list, num)
                delIndex(skaters_list, i)
                break
            else:
                count += countSkaters(skates_list, skaters_list, i, num)
                delIndex(skates_list, num)
                delIndex(skaters_list, i)
                break
    if flag:
        delIndex(skaters_list, i)
print('\nНаибольшее кол-во людей, которые могут взять ролики: ', count)




# #Кол-во коньков: 4
# Размер 1 пары: 41
# Размер 2 пары: 40
# Размер 3 пары: 39
# Размер 4 пары: 42
#
# Кол-во людей: 3
# Размер ноги 1 человека: 42
# Размер ноги 2 человека: 41
# Размер ноги 3 человека: 42
#
# Наибольшее кол-во людей, которые могут взять ролики: 2