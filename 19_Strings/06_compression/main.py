str_text = input('Введите строку: ')
new_str = ''
start_str = str_text[0]
count = 0
for i_elem in str_text:
    if i_elem != start_str:
        new_str += start_str + str(count)
        start_str = i_elem
        count = 1
    else:
        count += 1

print(new_str + start_str + str(count))
