import random


def save_sum_file(num):
    with open('file777.txt', 'a') as save_file_777:
        save_file_777.write(num)
        save_file_777.write('\n')


sum_num = 0
while True:
    number = input('Введите число: ')
    sum_num += int(number)
    save_sum_file(number)
    if sum_num >= 777:
        print('Сумма больше или равна 777')
        break
    rand_num = random.randint(1, 13)
    print(rand_num)
    if rand_num == 1:
        print('Выпало случайное исключение, программа завершена')
        break
