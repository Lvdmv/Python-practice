# n = int(input('Введите кол-во чисел: '))
# digit_list = []
# for i in range(n):
#     digit = int(input('Введите число: '))
#     digit_list.append(digit)
# print('Изначальный список:', digit_list)
# index = 0
# count = 0
# for _ in range(n):
#     minNum = digit_list[count]
#     for j in range(n - count):
#         if minNum > digit_list[j + count]:
#             minNum = digit_list[count + j]
#             index = count + j
#     digit_list[index] = digit_list[count]
#     digit_list[count] = minNum
#     count += 1
#     index = count
# print('Отсортированный список:', digit_list)


# def selection_sort(my_list):
#     for i_am in range(len(my_list)):
#         for curr in range(i_am, len(my_list)):
#             if my_list[curr] < my_list[i_am]:
#                 my_list[i_am], my_list[curr] = my_list[curr], my_list[i_am]
#
#
#
#
# nums = [1, 4, -3, 0, 10]
#
# selection_sort(nums)
#
# print(nums)
