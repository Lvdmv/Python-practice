friends_amt = int(input('Кол-во друзей: '))
credit_amt = int(input('Долговых расписок: '))
friends_list = []
for i_friend in range(friends_amt):
    friends_list.append(list([i_friend + 1, 0]))
for i_amt in range(credit_amt):
    print()
    print(i_amt + 1, 'расписка')
    whom = int(input('Кому: '))
    who = int(input('От кого: '))
    how_match = int(input('Сколько: '))
    friends_list[whom - 1][1] -= how_match
    friends_list[who - 1][1] += how_match
print('\nБаланс друзей: ')
for i_amt in range(friends_amt):
    print(friends_list[i_amt][0], ':', friends_list[i_amt][1])


