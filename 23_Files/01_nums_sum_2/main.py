numbers_file = open('numbers.txt', 'r')
data = numbers_file.read()
print('Содержимое файла numbers.txt')
print(data)
summ = 0
for i_num in data:
    if i_num.isdigit():
        summ += int(i_num)
print()
numbers_file.close()
counts_file = open('answer.txt', 'w')
counts_file.write(str(summ))
print('Содержимое файла answer.txt')
print(summ)
counts_file.close()
