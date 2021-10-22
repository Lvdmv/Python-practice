def min_len(my_elem, my_elem2):
    return min(len(my_elem), len(my_elem2))


new_string = 'abcd'
new_tuple = (10, 20, 30, 40)
#
print(i for i in zip(new_string, new_tuple))
a = (i for i in zip(new_string, new_tuple))
for i in a:
    print(i)
#
new_list = ((new_string[i], new_tuple[i]) for i in range(min_len(new_string, new_tuple)))

for j in new_list:
    print(j)
