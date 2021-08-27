word = input('Введите строку содержащую букву h минимум два раза: ')
print(word[((len(word) - 2) - word[::-1].index('h')) : word.index('h') : -1])
