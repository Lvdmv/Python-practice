films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
like_film = []
count = 0
for _ in films:
    count += 1
for _ in range(count):
    flag = False
    new_film = input('Введите название любимого фильма: ')
    for i in films:
        if new_film == i:
            like_film.append(new_film)
            flag = True
    if flag == False:
        print('Ошибка! Такого фильма нет в списке.')

print('Список любимых фильмов:', like_film)

