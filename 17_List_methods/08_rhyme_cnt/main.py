def delIndex(my_list, index):
  nextIndex = index % len(my_list)
  return nextIndex

n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый ', k, 'человек')
n_list = list(range(1, n + 1))
startIndex = 0
start = 0
dell = 0
while len(n_list) != 1:
  print('Текущий круг:', n_list)
  print('Начало счёта с номера: ', n_list[startIndex])
  print('Будет удалена: ', n_list[delIndex(n_list, k + startIndex-1)])
  start = delIndex(n_list, k + startIndex-1)
  n_list.remove(n_list[delIndex(n_list, k + startIndex-1)])
  if start <= len(n_list)-1:
    startIndex = start
  else:
     startIndex = 0
print('Останется число: ', n_list[0])
