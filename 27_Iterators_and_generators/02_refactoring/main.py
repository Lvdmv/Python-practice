from collections.abc import Iterable


def find_num(number: int) -> Iterable[int]:
    for x in list_1:
        for y in list_2:
            result = x * y
            yield f'{x} {y} {result}'
            if result == number:
                print('Found!!!')
                return


list_1 = [2, 5, 7, 10]
list_2 = [3, 8, 4, 9]
for i_pair in find_num(56):
    print(i_pair)
