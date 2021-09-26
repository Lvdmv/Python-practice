
def simmetrical_str(my_str):
    new_list = [i_str for i_str in my_str]
    if len(set(my_str)) % len(new_list) != len(set(my_str)):
        return False
    else:
        return True

new_str = input('Введите строку: ')
if new_str == new_str[::-1]:
    print('Можно сделать палиндромом')
elif simmetrical_str(new_str):
    print('Можно сделать палиндромом')
else:
    print('Нельзя сделать палиндромом')