def counter(count, my_list, index):
    for i_count in range(count - 1):
        my_list.remove(index)

def selection_sort(my_list):
    for i_am in range(len(my_list)):
        for curr in range(i_am, len(my_list)):
            if my_list[curr] < my_list[i_am]:
                my_list[i_am], my_list[curr] = my_list[curr], my_list[i_am]


classFirst = list(range(160, 177, 2))
classSecond = list(range(162, 181, 3))
classFirst.extend(classSecond)

for i in range(len(classFirst)):
    flag = False
    for num in range(i + 1, len(classFirst)):
        if classFirst[i] == classFirst[num]:
            flag = True
    if flag:
        counter(classFirst.count(classFirst[i]), classFirst, classFirst[i])
selection_sort(classFirst)
print(classFirst)

