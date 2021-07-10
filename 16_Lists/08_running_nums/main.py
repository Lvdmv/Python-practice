k = int(input('Сдвиг: '))
n = int(input('Введите кол-во элементов в списке: '))
normal_list = []
shifted_list = []
for i in range(n):
    element = int(input('Введите элемент списка: '))
    normal_list.append(element)
for i in range(n):
    shifted_list.append(normal_list[i - k])
print('Изначальный список: ', normal_list)
print('Сдвинутый список: ', shifted_list)