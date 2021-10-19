students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

def listInterest_lenSurname(my_dict):
    lst_int = []
    len_surname = 0
    for i_value in my_dict.values():
        lst_int.extend(i_value['interests'])
        len_surname += len(i_value['surname'])
    return lst_int, len_surname

pairs = [(f'{i_id} - {i_age["age"]}') for i_id, i_age in students.items()]
print(pairs)

interest_lst, length_surname = listInterest_lenSurname(students)
print(interest_lst, length_surname)

