import os


def find_size_file(cur_path):
    for i_elem in os.listdir(cur_path):
        path = os.path.join(cur_path, i_elem)
        if os.path.isdir(path):
            count_dict['direct'] += 1
            find_size_file(path)
        else:
            count_dict['file'] += 1
            count_dict['size_file'] += os.path.getsize(path)


count_dict = {'file': 0, 'direct': 0, 'size_file': 0}
count_size_file = find_size_file(os.path.abspath(os.path.join('..', '..', '..', 'pythonProject')))
print(f'Размер каталога (в Кб): {count_dict["size_file"] / 1024}')
print(f'Количество подкаталогов: {count_dict["direct"]}')
print(f'Количество файлов: {count_dict["file"]}')
