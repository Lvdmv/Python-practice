class TaskManager:
    def __init__(self):
        self.my_dict = dict()

    def info(self):
        for i_key, i_value in sorted(self.my_dict.items()):
            print(i_key, '; '.join(i_value))

    def new_task(self, value, key):
        if key in self.my_dict:
            self.my_dict[key].append(value)
        else:
            self.my_dict[key] = [value]

    def del_task(self, key):
        self.my_dict.pop(key, None)


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)

manager.info()
manager.del_task(2)
print()
manager.info()
