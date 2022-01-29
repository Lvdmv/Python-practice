from collections.abc import Iterable
from typing import Any
import os


def str_count(file: Any) -> int:
    counter = 0
    with open(f'{file}', 'r', encoding='utf-8') as file_py:
        for i_str in file_py:
            if len(i_str) != 0:
                if not i_str.startswith('#'):
                    counter += 1
    print(f'Файл содержит {counter} строчек кода\n')
    return counter


def find_file(cur_path: Any) -> Iterable[Any]:
    try:
        print('переходим в', cur_path)
        for i_elem in os.listdir(cur_path):
            path = os.path.join(cur_path, i_elem)
            print(f'смотрим {path}')
            if os.path.isdir(path):
                print('это директория')
                for i_file in find_file(path):
                    yield i_file
            elif i_elem.endswith('.py'):
                print('\nЭто питоновский файл')
                yield path
            else:
                print('Это не питоновский файл')
    except PermissionError:
        print('Ошибка доступа к файлу')


print(
    '\nОбщее кол-во строк кода: ', sum(
        [
            str_count(i) for i in find_file(
                os.path.abspath(
                    os.path.join(
                        '..', '..', '..', input(
                            'Введите название директории: '
                        )
                    )
                )
            )
        ]
    )
)
