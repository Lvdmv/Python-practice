alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = input('Введите текст: ')
k = int(input('Введите сдвиг: '))

caesar_cipher = [(alphabet[(alphabet.index(j) + k) % len(alphabet)] if j != ' ' else ' ')
          for j in text]

for i in caesar_cipher:
    print(i, end='')