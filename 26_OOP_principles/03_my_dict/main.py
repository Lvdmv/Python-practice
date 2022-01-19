class MyDict:
    def __init__(self):
        self.my_dict = dict()

    def info(self):
        print(self.my_dict)

    def save_in_dict(self, key, value):
        self.my_dict[key] = value

    def get(self, key):
        return self.my_dict.get(key, 0)

my_dict = MyDict()
my_dict.save_in_dict(1, 2)
print(my_dict.get(1))


#
# class MyDict(dict):
#     def get(self, key, default=0):
#         return super().get(key, default)
#
#
# my_dict = MyDict()
# my_dict[1] = 2
# print(my_dict.get(1))


