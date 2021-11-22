site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iphone',
            'div': 'Купить',
            'p': 'продать'
        }
    }
}


def print_key(new_key, counter, name):
    counter += 4
    for i_key, i_value in new_key.items():
        if i_key == 'title':
            i_value = f'Куплю/продам {name} недорого'
        if i_key == 'h2':
            i_value = f'У нас самая низкая цена на {name}'
        if isinstance(i_value, dict):
            print(f'{" " * counter} {i_key} : ', end='{\n')
            print_key(i_value, counter, name)
        else:
            print(f'{" " * counter} {i_key} : {i_value}')
    print(f'{" " * (counter-4)}', "}")


def is_phone(new_dict, num):
    count = 0
    if num != 0:
        name_product = input('Введите название продукта для нового сайта: ')
        if name_product not in site_list:
            site_list.append(name_product)
        for site_name in site_list[::]:
            print(f'\nСайт для {site_name}:')
            print('site = {')
            print_key(new_dict, count, site_name)
            is_phone(new_dict, num - 1)


site_list = []
amt_site = int(input('Сколько сайтов: '))
is_phone(site, amt_site)
