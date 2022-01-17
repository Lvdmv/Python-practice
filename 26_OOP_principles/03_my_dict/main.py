class MyDict:
    def __init__(self):
        self.my_dict = dict()

    def info(self):
        print(self.my_dict)

    def save_in_dict(self, key, value):
        self.my_dict[key] = value

    def get(self, key):
        if key in self.my_dict:
            print(self.my_dict.get(key))
        else:
            print(0)


my_dict = MyDict()
my_dict.save_in_dict(1, 2)
my_dict.get(1)
