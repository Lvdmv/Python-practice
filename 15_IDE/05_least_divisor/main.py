n = int(input('Введите число: '))
count = 2
while n % count != 0:
    if count == 9:
        count = n
        break
    else:
        count += 1
print('Наименьший делитель, отличный от единицы:', count)