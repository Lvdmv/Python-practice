import zipfile


def count_dict_let(letter):
    if letter.isalpha():
        if letter not in dict_letter:
            dict_letter[letter] = 1
        else:
            dict_letter[letter] += 1


voina_i_mir_zip = zipfile.ZipFile('voyna-i-mir.zip', 'r')
voina_i_mir = open(voina_i_mir_zip.extract('voyna-i-mir.txt'), 'r', encoding='utf-8')
dict_letter = dict()
count_letter = 0

for i_letter in voina_i_mir.read():
    if i_letter.isalpha():
        count_dict_let(i_letter)
        count_letter += 1

share_latt = []
for i_share in sorted(dict_letter, key=dict_letter.get, reverse=True):
    share_latt.append(f'{i_share} {dict_letter[i_share]}')
list_share_latt = '\n'.join(share_latt)

an_file_voina_i_mir = open('an_file_voina_i_mir.txt', 'w', encoding='utf-8')
an_file_voina_i_mir.write(list_share_latt)
an_file_voina_i_mir.close()

an_file_voina_i_mir = open('an_file_voina_i_mir.txt', 'r', encoding='utf-8')
print(f'\nСодержимое файла an_file_voina_i_mir.txt: \n{an_file_voina_i_mir.read()}')
an_file_voina_i_mir.close()
