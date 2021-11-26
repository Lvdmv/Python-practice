import os


def record_file(path, new_data):
    file = open(path, 'w')
    file.write(new_data)
    print('Файл успешно сохранён!')
    file.close()


def file_actions(cur_path, is_file_name, new_data):
    if os.path.exists(cur_path):
        path = os.path.join(cur_path, is_file_name)
        if os.path.exists(path):
            answer = input('Вы действительно хотите перезаписать файл? да/нет')
            if answer.lower() == 'да':
                record_file(path, new_data)
            else:
                return None
        else:
            record_file(path, new_data)
    else:
        print(f'Пути {cur_path} нет на диске')

new_str = input('Введите строку: ')
print('Куда хотите сохранить документ? Введите последовательность папок (через пробел):')
sequence_dir = input().split()
print(', '.join(sequence_dir))

file_path = os.path.join('C:/', '/'.join(sequence_dir))
print(file_path)
file_name = input('Введите имя файла: ')
do_file = file_actions(file_path, file_name, new_str)
file_contents = open(os.path.join(file_path, file_name), 'r')
print('\nСодержимое файла:', file_contents.read())
file_contents.close()
