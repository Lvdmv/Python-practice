vowels = 'аиеёоуыэюя'
text = input('Введите текст: ')
list = [text[i] for i in range(len(text)) for j in range(len(vowels)) if text[i] == vowels[j]]
print('Список гласных букв: ',list)
print('Длина списка: ', len(list))
