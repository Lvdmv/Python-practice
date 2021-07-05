
def summNum(number):
    summ = 0
    while number != 0:
        summ = number % 10
        number //= 10
    return summ

def countNum(number):
    count = 0
    while number != 0:
        number //= 10
        count += 1
    return count


n = int(input('Введите число: '))
print('Сумма цифр:', summNum(n))
print('Кол-во цифр в числе:', countNum(n))
print('Разность суммы и кол-ва цифр:', summNum(n) - countNum(n))