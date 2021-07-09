n = int(input('Кол-во видеокарт: '))
videocard_list = []

for i in range(n):
  print(i + 1, 'Видеокарта: ', end ='')
  v_card = int(input())
  videocard_list.append(v_card)

maxCard = videocard_list[0]

for cardMaxnum in videocard_list:
  if cardMaxnum > maxCard:
    maxCard = cardMaxnum

newcard_list = []

for cardNum in videocard_list:
  if cardNum != maxCard:
    newcard_list.append(cardNum)

print('Старый список видеокарт:', videocard_list)
print('Новый список видеокарт:', newcard_list)


