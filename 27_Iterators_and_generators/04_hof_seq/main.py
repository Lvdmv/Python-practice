from typing import List
from collections.abc import Iterable


class EqualityError(Exception):
    pass


def qhofstadter(my_list: list) -> Iterable[list]:
    if my_list[0] != my_list[1]:
        raise EqualityError('Первый член последовательности должен быть равен второму')
    index_next = 1
    while True:
        if index_next < 3:
            yield 1
        else:
            value = my_list[index_next - my_list[index_next - 2] - 1] + my_list[index_next - my_list[index_next - 3] - 1]
            yield value
            my_list.append(value)
        index_next += 1


new_list = [1, 1]
for i in qhofstadter(new_list):
    try:
        print(i, end=' ')
    except EqualityError:
        break


class QHofstadter:
    def __init__(self, q_list: List[int]) -> None:
        self.q_list = q_list
        self.index_next = 0

    def __iter__(self) -> 'QHofstadter':
        self.index_next = 0
        return self

    def __next__(self) -> int:
        if self.q_list[0] != self.q_list[1]:
            raise EqualityError('Первый член последовательности должен быть равен второму')
        self.index_next += 1
        if self.index_next < 3:
            return 1
        else:
            value = self.q_list[
                        self.index_next - self.q_list[self.index_next - 2] - 1] + \
                    self.q_list[self.index_next - self.q_list[self.index_next - 3] - 1]
            self.q_list.append(value)
            return value


new_list = [1, 1]
q_object = QHofstadter(new_list)
for i in q_object:
    try:
        print(i, end=' ')
    except EqualityError:
        break
    try:
        print(i, end=' ')
    except EqualityError:
        break
