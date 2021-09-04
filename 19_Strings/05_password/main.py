password = input('Введите пароль: ')
if len(password) < 8:
    print('Пароль ненадёжный. Попробуйте ещё раз.')
elif sum([1 if i_elem.isupper() else 0 for i_elem in password]) < 1:
    print('Пароль ненадёжный. Попробуйте ещё раз.')
elif password.isalnum():
    if sum([1 if i_elem.isdigit() else 0 for i_elem in password]) < 3:
        print('Пароль ненадёжный. Попробуйте ещё раз.')
    else:
        print('Это надёжный пароль!')
