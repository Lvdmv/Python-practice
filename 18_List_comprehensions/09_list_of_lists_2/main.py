nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]

new_list = []
nice_list = [[new_list.extend(x) for x in nice_list[0]], [new_list.extend(x) for x in nice_list[1]]]
print(new_list)
