def simmetrical_seq(my_list):
    new_list = ''
    for i in my_list:
        new_list = i + new_list
    return new_list

num_amt = int(input('Кол-во чисел: '))
seq_list = ''
for _ in range(num_amt):
    print('Число: ', end = ' ')
    digit = input()
    seq_list += digit
count = 0
add_digit = ''
new_list = simmetrical_seq(seq_list)
new_seq_list = seq_list
for i_digit in new_list:
    if count > 0:
        new_seq_list += i_digit
        add_digit += i_digit
        if simmetrical_seq(new_seq_list) == new_seq_list:
            break
    count += 1
new_seq_list = seq_list
count1 = 1
add_digit1 = ''
for i_digit in seq_list:
    new_seq_list += i_digit
    add_digit1 += i_digit
    if simmetrical_seq(new_seq_list) == new_seq_list:
        break
    count1 += 1
print('Последовательность: ', seq_list)
if  count < count1:
    print('Нужно приписать чисел: ', count)
    print('Сами числа: ', add_digit)
else:
    print('Нужно приписать чисел: ', count1)
    print('Сами числа: ', add_digit1)








# #Кол-во чисел: 5
# Число: 1
# Число: 2
# Число: 1
# Число: 2
# Число: 2
#
# Последовательность: 1 2 1 2 2
# Нужно приписать чисел: 3
# Сами числа: 1 2 1

