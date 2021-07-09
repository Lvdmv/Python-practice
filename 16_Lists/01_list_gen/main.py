n = int(input('Сколько всего чисел? '))
countOddnum =[]
for i in range(1, n + 1):
  if i % 2 != 0:
    countOddnum.append(i)
print('В списке чисел от 1 до', n, 'содержутся следующие нечетные числа:', countOddnum)