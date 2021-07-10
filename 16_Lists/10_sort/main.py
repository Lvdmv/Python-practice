n = int(input('Введите кол-во чисел: '))
digit_list = []
for i in range(n):
    digit = int(input('Введите число: '))
    digit_list.append(digit)
print('Изначальный список:', digit_list)
index = 0
count = 0
for _ in range(n):
    minNum = digit_list[count]
    for j in range(n - count):
        if minNum > digit_list[j + count]:
            minNum = digit_list[count + j]
            index = count + j
    digit_list[index] = digit_list[count]
    digit_list[count] = minNum
    count += 1
    index = count
print('Отсортированный список:', digit_list)