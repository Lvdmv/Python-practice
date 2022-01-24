from collections.abc import Iterable
from typing import Any
import os


def find_file(cur_path: Any, file_name: str) -> Iterable[Any]:
    try:
        print('переходим в', cur_path)
        for i_elem in os.listdir(cur_path):
            path = os.path.join(cur_path, i_elem)
            if file_name == i_elem:
                print('\nКаталог найден')
                print(f'Путь к каталогу: {path}')
                return
            yield f'смотрим {path}'
            if os.path.isdir(path):
                print('это директория')
                for i_file in find_file(path, file_name):
                    yield i_file
            else:
                print('Каталог не найден')
    except PermissionError:
        print('Ошибка доступа к файлу')


for i_path in find_file(os.path.abspath(os.path.sep), input('Введите название каталога: ')):
    print(i_path)
