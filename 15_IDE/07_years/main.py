
def sameNum(n1, n2):
    year = 0
    print('Года от', n1, 'до', n2, 'с тремя одинаковыми цифрами:', end = '\n')
    for i in range(n1, n2 + 1, 1):
        year = countNum(i)
        if year == 3:
            print(i, end = '\n')


def countNum(i):
    part1 = i % 10
    part2 = (i % 100) // 10
    count = 0
    count2 = 0
    while i > 0:
        if part1 == i % 10:
            count += 1
        elif part2 == i % 10:
            count2 += 1
        i //= 10
    if count == 3:
        return count
    elif count2 == 3:
        return count2
    else:
        return 0


a = int(input('Введите начальный год: '))
b = int(input('Введите конечный год: '))
sameNum(a, b)