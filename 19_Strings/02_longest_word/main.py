str_text = input('Введите строку содержащую пробелы: ')

max_len = str_text.split()[0]

for i in str_text.split(' '):
   if len(i) > len(max_len):
        max_len = i

print('Самое длинное слово в строке: ', max_len)