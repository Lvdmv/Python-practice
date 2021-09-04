str_ip = input('Введите IP: ')
if len(str_ip.split('.')) != 4:
    print('Адрес - это четыре числа, разделённые точками')

elif [i_elem for i_elem in str_ip.split('.') if not i_elem.isdigit()]:
    print(' '.join([i_elem for i_elem in str_ip.split('.') if not i_elem.isdigit()]), '- не целое число')

elif [i_elem for i_elem in str_ip.split('.') if int(i_elem) > 255]:
    print(' '.join([i_elem for i_elem in str_ip.split('.') if int(i_elem) > 255]), 'превышает 255')
else:
    print('IP-адрес корректен')

print(str_ip)