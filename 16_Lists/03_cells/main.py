n = int(input('Введите кол-во клеток: '))
cage_list =[]
for i in range(n):
  print('Эффективность', i + 1, 'клетки:', end ='')
  cage_effect = int(input())
  cage_list.append(cage_effect)
print('\nНеподходящие значения: ', end =' ')
for i in range(n):
  if  cage_list[i] < i + 1:
    print(cage_list[i], end=' ')
