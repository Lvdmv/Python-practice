def fibonachi_sequence(num_pos):
    if num_pos == 0:
        return 0
    if num_pos == -1:
        return 1
    new_num = fibonachi_sequence(num_pos-1)
    priveous_num = fibonachi_sequence(num_pos -2)
    return  new_num + priveous_num


print(fibonachi_sequence(28))

