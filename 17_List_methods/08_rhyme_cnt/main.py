def delIndex(startIndex, k, my_list):
    if k >= len(my_list):
        nextIndex = startIndex + k - (k // len(my_list)) * len(my_list) - 1
        while nextIndex > len(my_list) - 1:
            nextIndex -= len(my_list)
    else:
        nextIndex = startIndex + k - 1
        while nextIndex > len(my_list) - 1:
            nextIndex -= len(my_list)
    return nextIndex

def startPoint(k, my_list):
    n = delIndex(startIndex, k, n_list)
    if n != len(my_list) - 1 and n > 0:
      return n
    else:
      return 0

n = int(input('Кол-во человек: '))
k = int(input('Какое число в считалке? '))
print('Значит, выбывает каждый ', k, 'человек')
n_list = list(range(1, n + 1))
startIndex= 0
start = 0
while len(n_list) != 1:
  print('Текущий круг:', n_list)
  print('Начало счёта с номера', n_list[startIndex])
  dell = n_list[delIndex(startIndex, k, n_list)]
  print('Выбывает человек под номером', dell)
  start = startPoint(k, n_list)
  n_list.remove(dell)
  startIndex = start

print('\nОстался человек под номером', n_list[0])
