def zip_function(object1, object2, length):
    if length == 0:
        return 0
    zip_function(object1, object2, length - 1)
    print((object1[length-1], object2[length-1]))


def min_len(my_elem, my_elem2):
    return min(len(my_elem), len(my_elem2))


new_string = 'abcd'
new_tuple = (10, 20, 30, 40)
zip_function(new_string, new_tuple, min_len(new_string, new_tuple))
