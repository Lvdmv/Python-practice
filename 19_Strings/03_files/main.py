name_file = input('Введите имя файла: ')
extension = '.txt', '.docx'
if not name_file[0].isalpha():
    print('Ошибка: название начинается на один из специальных символов')
elif not name_file.endswith(extension):
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
else:
    print('Файл назван верно.')
