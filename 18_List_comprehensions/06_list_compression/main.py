import random
n = int(input('Введите кол-во элементов списка: '))
nums = [random.randint(0, 9) for _ in range(n)]
new_nums = [x for x in nums if x != 0]
zero_list = new_nums[:]
zero_list.extend([0] * (n - len(new_nums)))

print('Исходный список: ', nums)
print('Упорядоченный список: ', zero_list)
print('Сжатый список: ', new_nums)
