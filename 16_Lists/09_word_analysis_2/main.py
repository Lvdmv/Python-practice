word = input('Введите слово: ')
word_list = list(word)
palindrome = []
for i in range(1, len(word_list) + 1):
    palindrome.append(word_list[-i])
if palindrome == word_list:
    print('Слово является палиндромом')
