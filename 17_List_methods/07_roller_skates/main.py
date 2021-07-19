
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
for i in sorted(skaters_list):
    for num in sorted(skates_list):
        if i == num:
          if skaters_list.count(i) <= skates_list.count(num):
              count += skaters_list.count(i)
              index = i
          else:
              count += skates_list.count(num)
              index = num
          for _ in range(skaters_list.count(index)):
              skaters_list.remove(index)
          index = 0
          break

print('\nНаибольшее кол-во людей, которые могут взять ролики: ', count)



