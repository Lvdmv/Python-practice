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


def function(name):
    site['html']['head']['title'] = f'Куплю/продам {name} недорого'
    site['html']['body']['h2'] = f'У нас самая низкая цена на {name}'
    if name not in dict_site:
        dict_site[name] = str(site)
        for i in dict_site.keys():
            print(f'\nСайт для {i}:')
            print('site =', dict_site[i])
            print()


def key_position(counter):
    if counter == 0:
        return None
    name_product = input('Введите название продукта для нового сайта: ')
    function(name_product)
    key_position(counter - 1)
    function(name_product)


dict_site = dict()
amt_site = int(input('Сколько сайтов: '))
key_position(amt_site)
