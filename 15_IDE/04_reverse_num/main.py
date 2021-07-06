
def countNum(num):
    flag = False
    partFirst = ''
    partLast = ''
    for i in num:
        if i != '.':
            if flag == False:
                partFirst = i + partFirst
            else:
                partLast = i + partLast
        else:
            flag = True
            partFirst += i
    number = partFirst + partLast
    return number




first_n = input('Введите первое число: ')
second_n = input('Введите второе число: ')
print('Первое число наоборот:', countNum(first_n))
print('Второе число наоборот:', countNum(second_n))
first_n = float(countNum(first_n))
second_n = float(countNum(second_n))

print('Сумма:', first_n + second_n)