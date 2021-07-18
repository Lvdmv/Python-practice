shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300],
        ['педаль', 100], ['седло', 1500], ['рама', 12000],
        ['обод', 2000], ['шатун', 200], ['седло', 2700]]

detail = input('Название детали: ')
counter = [0, 0]

for i_prace in range(len(shop)):
        flag = True
        if shop[i_prace][0] == detail:
                flag = False
                counter[0] += shop[i_prace][1]
                counter[1] += 1
if flag:
        print('Такой детали нет в наличии.')
else:
        print('Кол-во деталей: ', counter[1])
        print('Общая стоимость: ', counter[0])
