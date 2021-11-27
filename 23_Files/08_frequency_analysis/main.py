text = input('Введите текст: ')
text_file = open('first_tour.txt', 'w')
text_file.write(text)
text_file.close()

text_file = open('first_tour.txt', 'r')
print(f'Содержимое файла text.txt: \n{text_file.read()}')
text_file.close()


def count_dict_let(letter):
    if letter.isalpha():
        if letter not in dict_letter:
            dict_letter[letter] = 1
        else:
            dict_letter[letter] += 1


text_file = open('first_tour.txt', 'r')
dict_letter = dict()
count_letter = 0

for i_letter in text_file.read().lower():
    if i_letter.isalpha():
        count_dict_let(i_letter)
        count_letter += 1
text_file.close()

share_latt = []
for i_share in sorted(dict_letter, key=dict_letter.get, reverse=True):
    share_latt.append(f'{i_share} {round(dict_letter[i_share]/count_letter, 3)}')
list_share_latt = '\n'.join(share_latt)

analysis_file = open('analysis.txt', 'w')
analysis_file.write(list_share_latt)
analysis_file.close()

analysis_file = open('analysis.txt', 'r')
print(f'\nСодержимое файла analysis.txt: \n{analysis_file.read()}')
analysis_file.close()
