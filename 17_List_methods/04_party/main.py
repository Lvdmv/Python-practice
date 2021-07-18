guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

print('Сейчас на вечеринке', len(guests), 'человек:', guests)
text = input('Гость пришел или ушел? ')
while text != 'Пора спать':
    if text == 'пришел':
        name_guests = input('Имя гостя: ')
        if len(guests) < 6:
            guests.append(name_guests)
            print('Привет, ', name_guests + '!')
        else:
            print('Прости,', name_guests + ',', 'но мест нет.')
    elif text == 'ушел':
        name_guests = input('Имя гостя: ')
        guests.remove(name_guests)
        print('Пока, ', name_guests + '!')
    print('\nСейчас на вечеринке', len(guests), 'человек:', guests)
    text = input('Гость пришел или ушел? ')

print('\nВечеринка закончилась, все легли спать.')
