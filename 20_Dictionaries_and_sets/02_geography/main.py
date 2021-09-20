def city_location(city):
    for i_city in dict_country.values():
        if city in i_city:
            return i_city
    else:
        return False

amt_countries = int(input('Кол-во стран: '))

dict_country = dict()

for i_country in range(amt_countries):
    print(i_country + 1, 'страна: ', end = '')
    country_and_city = input()
    dict_country[country_and_city.split()[0]] = country_and_city.split()[1:]

for i_num in range(3):
    print()
    print(i_num + 1, 'город: ', end= '')
    city = input()
    if city_location(city):
        print('Город', city, 'расположен в стране', ''.join({i_key for i_key in dict_country.keys() if dict_country[i_key] == city_location(city)}) + '.')
    else:
        print('По городу', city, 'данных нет.')

