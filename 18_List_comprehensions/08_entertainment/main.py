import random
n =int(input('Кол-во палок: '))
k = int(input('Кол-во бросков: '))
my_list = list('I' * n)

for i_k in range(k):
    print('Бросок', i_k + 1, end = ' ')
    a = random.randint(1, n)
    b = random.randint(a, n)
    print('Сбиты палки с номера', a, '\nпо номер', b)
    if b > a:
      my_list[a - 1:b] = '.' * (b + 1 - a)
    else:
      my_list[a - 1:b] = '.'

print('\nРезультат: ', end='')
for i in my_list:
    print(i, end='')
