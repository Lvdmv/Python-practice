class Node:
    def __init__(self, number):
        self.number = number
        self.next_num = None

    def __str__(self):
        return str(self.number) + ' '


class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def __str__(self):
        if self.head is None:
            return []
        last_num = self.head
        new_str = str(last_num)
        while last_num.next_num:
            last_num = last_num.next_num
            new_str += f'{last_num}'
        return f'[{" ".join(new_str.split())}]'

    def append(self, elem: int) -> None:
        new_num = Node(elem)
        if self.head is None:
            self.head = new_num
            return
        last_num = self.head
        while last_num.next_num:
            last_num = last_num.next_num
        last_num.next_num = new_num

    def get(self, index):
        last_num = self.head
        node_index = 0
        while node_index <= index:
            if node_index == index:
                return last_num.number
            node_index += 1
            last_num = last_num.next_num

    def remove(self, index):
        last_num = self.head
        node_index = 0
        while node_index <= index:
            if node_index == index:
                last_num.number = ''
                break
            node_index += 1
            last_num = last_num.next_num


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
