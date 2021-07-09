team_list =['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
evenCount = []
print('Состав команды: ', end ='\n')
for i in range(8):
  if i % 2 == 0:
    print(team_list[i])
