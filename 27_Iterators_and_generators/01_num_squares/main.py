from collections.abc import Iterable


def square(number: int) -> Iterable[int]:
    cur_val = 1
    for _ in range(number):
        yield cur_val ** 2
        cur_val += 1


for i_sce in square(5):
    print(i_sce, end=' ')
print()


class Square:
    def __init__(self, number: int) -> None:
        self.limit = number
        self.cur_val = 0

    def __iter__(self) -> 'Square':
        self.cur_val = 0
        return self

    def __next__(self) -> int:
        if self.cur_val < self.limit:
            self.cur_val += 1
            return self.cur_val ** 2
        raise StopIteration


seq_squares = Square(5)
for i_sce in seq_squares:
    print(i_sce, end=' ')
print()


[print(i_square ** 2, end=' ') for i_square in range(1, 6)]
