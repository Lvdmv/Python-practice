import random

# Первый вариант:
def pair_tuple(my_list):
   tuple_even = []
   tuple_odd = []
   for i, j in enumerate(my_list):
       if i % 2 == 0:
         tuple_even.append(j)
       else:
          tuple_odd.append(j)
   new_tuple = zip(tuple_even, tuple_odd)
   new_tuple = list(new_tuple)
   return new_tuple

# Второй вариант:
def pair_tuple(my_list):
    return list(zip(my_list[::2], my_list[1::2]))


origin_list = sorted([random.randint(0, 10) for _ in range(10)])

print('Оригинальный список', origin_list)
print('Новый список', pair_tuple(origin_list))


