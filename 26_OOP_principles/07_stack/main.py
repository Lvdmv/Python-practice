class Stack:
    def __init__(self):
        self.__my_list = []

    def __str__(self):
        return '; '.join(self.__my_list)

    def app_list(self, elem):
        self.__my_list.append(elem)

    def pop(self):
        if len(self.__my_list) != 0:
            return self.__my_list.pop()
        else:
            return None


class TaskManager:
    def __init__(self):
        self.my_dict = dict()

    def __str__(self):
        show_list = []
        for i_key, i_value in sorted(self.my_dict.items()):
            show_list.append(f'{i_key} {i_value}\n')
        return ''.join(show_list)

    def new_task(self, value, key):
        if key not in self.my_dict:
            self.my_dict[key] = Stack()
        self.my_dict[key].app_list(value)

    def pop(self, key):
        if key in self.my_dict:
            return self.my_dict[key].pop()
        return None


# stack = Stack()
# for i_num in range(4):
#     stack.app_list(i_num)
# print(stack)
# stack.pop()
# print(stack)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

print(manager)
manager.pop(3)
print(manager)
