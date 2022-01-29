class LinkedList:
    def __init__(self) -> None:
        self.__str = ''

    def __str__(self) -> str:
        return f'[{" ".join(self.__str.split())}]'

    def append(self, elem: int) -> None:
        self.__str += ' ' + str(elem)

    def get(self, index: int) -> str:
        new_str = ''
        count = 0
        for i_index, i_str in enumerate(self.__str):
            if i_str == ' ':
                count += 1
            if count == index + 1:
                if i_str != ' ':
                    new_str += i_str
        return new_str

    def remove(self, index: int) -> None:
        new_str = ''
        count = 0
        for i_index, i_str in enumerate(self.__str):
            if i_str == ' ':
                count += 1
            if count != index + 1:
                new_str += i_str
        self.__str = new_str


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
