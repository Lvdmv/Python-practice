
print('Введите координаты монетки:')
x = float(input('X: '))
y = float(input('Y: '))
r = int(input('Введите радиус: '))
if r >= x and r >= y:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')
