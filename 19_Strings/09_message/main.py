def reverse_str(i_word):
    rev_word = ''
    revers = ' '
    flag = True
    for i in i_word:
        if i.isalpha() and flag:
            rev_word = i + rev_word
        elif not flag:
            revers = i + revers
        else:
            rev_word = rev_word + i
            flag = False
    return rev_word + revers

text = input('Сообщение: ')
print(''.join([reverse_str(i_elem) for i_elem in (''.join([i_elem for i_elem in list(text)]).split(' '))]))

