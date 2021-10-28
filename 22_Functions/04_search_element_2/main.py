site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


key_dict = input('Введите ключ словаря: ')


def key_position(my_key, my_dict):
    if my_key in my_dict:
        return my_dict[my_key]
    for i_position, i_info in my_dict.items():
        if isinstance(i_info, dict):
            search = key_position(my_key, i_info)
            if search:
                return search
    return None


print(key_position(key_dict, site))
