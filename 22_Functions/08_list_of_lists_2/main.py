def rectified_list(my_list, new_list = []):
    for i_num in my_list:
        if isinstance(i_num, list):
            rectified_list(i_num)
        else:
            new_list.append(i_num)
    return sorted(new_list)


nice_list = [1, 3, [2, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(rectified_list(nice_list))
