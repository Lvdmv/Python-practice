amt_order = int(input('Введите кол-во заказов: '))
order_base = dict()

for i_order in range(amt_order):
    print(i_order + 1, 'заказ: ', end = '')
    order = input().split()
    if not order[0] in order_base.keys():
        order_base[order[0]] = {order[1] : int(order[2])}
    elif not order[1] in order_base[order[0]]:
        order_base[order[0]][order[1]] = int(order[2])
    else:
        order_base[order[0]][order[1]] += int(order[2])


print()
for i_order_owner in sorted(order_base.keys()):
    print(i_order_owner + ':')
    for i_order in sorted(order_base[i_order_owner]):
        print('  ' + i_order + ':', order_base[i_order_owner][i_order])
