import os


def min_count_let(letter):
    if letter.lower() not in min_count_letter:
        min_count_letter[letter.lower()] = 1
    else:
        min_count_letter[letter.lower()] += 1


def count_lines(path):
    zen_list = open(path, 'r')
    amt_lines = 0
    amt_words = 0
    amt_letters = 0
    for i_line in zen_list:
        amt_lines += 1
        amt_words += count_words(i_line)
        amt_letters += count_letters(i_line)
    print('Кол-во строк:', amt_lines)
    print('Кол-во слов:', amt_words)
    print('Кол-во букв:', amt_letters)
    zen_list.close()


def count_words(line):
    count = 0
    for i_word in line.split():
        if count_letters(i_word):
            count += 1
    return count


def count_letters(line):
    count = 0
    for i_letter in line:
        if i_letter.isalpha():
            count += 1
            min_count_let(i_letter)
    return count


def find_file(cur_path, file_name):
    for i_elem in os.listdir(cur_path):
        path = os.path.abspath(os.path.join(cur_path, i_elem))
        if file_name == i_elem:
            count_lines(path)
        if os.path.isdir(path):
            find_file(path, file_name)


min_count_letter = dict()
find_name = find_file(os.path.abspath(os.path.join('..', '02_zen_of_python')), 'zen.txt')
print(f'Буква {min(min_count_letter, key=min_count_letter.get)} встречается наименьшее кол-во раз')
