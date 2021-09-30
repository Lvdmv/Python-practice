def counter(i_goods):
    summ = [0, 0]
    for i in range(len(store[goods[i_goods]])):
        summ[0] += store[goods[i_goods]][i]['quantity']
        summ[1] += store[goods[i_goods]][i]['quantity'] * store[goods[i_goods]][i]['price']
    return print(i_goods, '-',summ[0] , 'шт, стоимость ',summ[1], 'руб')

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


for i_goods in goods.keys():
    counter(i_goods)


