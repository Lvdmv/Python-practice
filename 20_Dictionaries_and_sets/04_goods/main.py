def counter(i_key):
    sum_quant = 0
    sum_prise = 0
    for i_store in store[goods[i_key]]:
        sum_quant += i_store['quantity']
        sum_prise += i_store['quantity'] * i_store['price']
    return f'{i_goods} - {sum_quant} шт, стоимость {sum_prise}'


goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


for i_goods in goods:
    print(counter(i_goods))
