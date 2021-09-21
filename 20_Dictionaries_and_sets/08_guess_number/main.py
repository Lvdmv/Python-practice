import random

max_num = int(input('Введите максимальное число: '))
num_set = {i for i in range(1, max_num + 1)}
conceived_num = random.randint(1, max_num)
print(conceived_num)

while True:
    print('Нужное число есть среди вот этих чисел: ', end = '')
    answer = input().lower()
    if answer == 'помогите!':
        print('Артём мог загадать следующие числа: ', end = '')
        for i_set in num_set:
            print(i_set, end = ' ')
        break
    elif answer == str(conceived_num):
        print('Ты угадал!')
        break
    elif str(conceived_num) in answer.split():
        print('Ответ Артёма: Да')
        for i_num in (num_set - set({int(str_num) for str_num in answer.split()})):
            num_set.discard(i_num)
    else:
        print('Ответ Артёма: Нет')
        for i_num in set({int(str_num) for str_num in answer.split()}):
            num_set.discard(i_num)


