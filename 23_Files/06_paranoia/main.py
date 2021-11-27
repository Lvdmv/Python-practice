def cipher_str(word, count):
    new_word = ''
    for i_letter in word:
        if i_letter.isalpha():
            if i_letter.isupper():
                new_word += (alfabet[(alfabet.index(i_letter.lower()) + count) % len(alfabet)].upper())
            else:
                new_word += (alfabet[(alfabet.index(i_letter) + count) % len(alfabet)])
    return new_word

alfabet = 'abcdefghijklmnopqrstuvwxyz'

file_text = open('text.txt', 'w')
list_text = []
for _ in range(4):
    list_text.append('Hello')
file_list_text = '\n'.join(list_text)
file_text.write(file_list_text)
file_text.close()

file_text = open('text.txt', 'r')
list_cipher = []
count_line = 0
for i_word in file_text:
    count_line += 1
    list_cipher.append(cipher_str(i_word, count_line))
new_list_cipher = '\n'.join(list_cipher)
file_text.close()

file_text = open('text.txt', 'r')
data = file_text.read()
print(f'Содержимое файла text.txt:\n{data}')
file_text.close()

new_file_text = open('cipher_text.txt', 'w')
new_file_text.write(new_list_cipher)
new_file_text.close()

new_file_text = open('cipher_text.txt', 'r')
print(f'\nСодержимое файла cipher_text.txt: \n{new_file_text.read()}')
new_file_text.close()
