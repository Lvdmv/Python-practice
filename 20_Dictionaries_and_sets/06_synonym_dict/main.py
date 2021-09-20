couple_words = int(input('Введите кол-во пар слов: '))

couple_dict = dict()
for i_word in range(couple_words):
    print(i_word + 1, 'пара: ', end = '')
    couple_word = input().split()
    couple_dict[couple_word[2]] = couple_word[0]
    couple_dict[couple_word[0]] = couple_word[2]
print(couple_dict)

while True:
    word = input('Введите слово: ').title()
    if couple_dict.get(word):
        print('Синоним: ', couple_dict[word])
        break
    else:
        print('Такого слова в словаре нет.')
