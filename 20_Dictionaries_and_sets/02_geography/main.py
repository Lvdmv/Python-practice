def city_location(my_dict, my_city):
    return ''.join({i_key for i_key in my_dict.keys() if my_city in my_dict[i_key]})

amt_countries = int(input('Кол-во стран: '))

dict_country = dict()

for i_country in range(amt_countries):
    print(i_country + 1, 'страна: ', end='')
    country_and_city = input().split()
    dict_country[country_and_city[0]] = country_and_city[1:]

for i_num in range(3):
    print()
    print(i_num + 1, 'город: ', end='')
    city = input()
    if city_location(dict_country, city):
        print(f'Город {city} расположен в стране {city_location(dict_country, city)}.')
    else:
        print(f'По городу {city} данных нет.')

