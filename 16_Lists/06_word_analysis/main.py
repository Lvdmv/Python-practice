word = input('Введите слово: ')
unique_list = list(word)
counter = len(unique_list)
countNum = [0, 0]
for num in range(counter):
    flag = True
    for i in unique_list:
        if unique_list[num] == i and countNum[0] != num:
            flag = False
        countNum[0] += 1
    countNum[0] = 0
    if flag:
        countNum[1] += 1
print('\nКол-во уникальных букв: ', countNum[1])