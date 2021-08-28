import random
first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
win_list = [max(first_team[i_elem], second_team[i_elem]) for i_elem in range(20)]
print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)
print('Победители тура: ', win_list)
