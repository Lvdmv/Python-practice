a = [1, 5, 3]
b = [1, 5, 1, 5]
c = [1, 3, 1, 5, 3, 3]
a.extend(b)
print('Кол-во цифр 5 при первом объединении:', a.count(5))
for i in range(a.count(5)):
    a.remove(5)
a.extend(c)
print('Кол-во цифр 3 при втором объединении:', a.count(3))
print('Итоговый список', a)

