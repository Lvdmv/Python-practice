def is_prime(number, length):
    return [i_prime for i_prime in range(2, length + 1) if (number % i_prime == 0 and number != i_prime) or number == 1]

def exam_prime(object):
    return [i_str for i_num, i_str in enumerate(object) if not is_prime(i_num, len(object))]

text_str = (100, 200, 300, 'буква', 0, 2, 'а')

if isinstance(text_str, tuple):
    print(f'Допустим, есть такой кортеж: {text_str}')
elif isinstance(text_str, dict):
    print(f'Допустим, есть такой словарь: {text_str}')
elif isinstance(text_str, str):
    print(f'Допустим, есть такая строка: {text_str}')
elif isinstance(text_str, list):
    print(f'Допустим, есть такой список: {text_str}')
print()
print(exam_prime(text_str))
