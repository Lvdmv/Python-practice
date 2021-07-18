
def twinsd(my_list):
      for i in range(len(my_list)):
          for num in range(i, len(my_list)):
              counter = 0
              num = my_list[i]
              counter = my_list.count(num)
              while counter > 1:
                  for i_am in range(counter - 1):
                      my_list.remove(num)
                  counter = 0

first_list = []
for i_first in range(3):
    print('Введите', i_first + 1, 'число: ', end = ' ')
    first = int(input())
    first_list.append(first)
print()
second_list = []
for i_second in range(7):
    print('Введите', i_second + 1, 'число: ', end = ' ')
    second = int(input())
    second_list.append(second)

first_list.extend(second_list)

twinsd(first_list)

print(first_list)