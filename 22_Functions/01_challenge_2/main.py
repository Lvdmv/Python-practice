def sequance_num(num):
    if num == 0:
        return 1
    sequance_num(num - 1)
    print(num, end=' ')


number = int(input('Введите число: '))
sequance_num(number)

