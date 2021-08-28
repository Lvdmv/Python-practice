vowels = 'аиеёоуыэюя'
text = input('Введите текст: ')
my_list = [i for i in text if i in vowels]
print('Список гласных букв: ',my_list)
print('Длина списка: ', len(my_list))
