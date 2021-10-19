def sorted_tuple(my_tuple):
    if {i for i in my_tuple if isinstance(i, float)}:
        return tuple(my_tuple)
    else:
        return tuple(sorted(my_tuple))


# origin_tuple = (1, 4, 3, 2)
origin_tuple = (1, 2, 3.0, 2)
# print(origin_tuple)
print(sorted_tuple(origin_tuple))