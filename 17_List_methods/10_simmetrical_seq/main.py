def simmetrical_seq(my_list):
    new_list = []
    for i in range(len(my_list)-1, -1, -1):
        new_list.append(my_list[i])
    if new_list == my_list:
        return True
    else:
        return False

num_amt = int(input('Кол-во чисел: '))
seq_list = []
count = 0
for _ in range(num_amt):
    print('Число: ', end = ' ')
    digit = int(input())
    seq_list.append(digit)
print('Последовательность: ', seq_list)
print('Сами числа: ', end = ' ')
while True:
    print(seq_list[0], end = ' ')
    count += 1
    seq_list.remove(seq_list[0])
    if simmetrical_seq(seq_list):
        break
print('\nНужно приписать чисел: ', count)


