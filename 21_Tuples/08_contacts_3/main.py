def is_contact(my_surname):
    return {i_contact for i_contact in phone_book if my_surname in i_contact}


phone_book = dict()
while True:
    answer = int(input('Добавить контакт или найти человека? 0/1 '))
    if answer == 0:
        name = input('Введите имя: ')
        surname = input('Введите фамилию: ')
        if (name, surname) in phone_book:
            print(f'{name} {surname} уже есть в списке контактов')
        else:
            num_phone = int(input('Введите номер телефона: '))
            phone_book[(name, surname)] = num_phone
            print(phone_book)
    else:
        new_surname = input('Введите фамилию контакта: ').title()
        if is_contact(new_surname):
            for i_person in is_contact(new_surname):
                print(' '.join(i_person), phone_book[i_person])
        else:
            print(f'Контакта с фамилией {new_surname} нет в телефонной книге')
