def calculating_math_func(data, fact_dict):
	if data in fact_dict:
		return fact_dict[data]
	result = 1
	for index in range(1, data + 1):
		result *= index
	result /= data ** 3
	result = result ** 10
	fact_dict[data] = result
	return result


new_dict = dict()
while True:
	num = int(input('Введите данные: '))
	print(calculating_math_func(num, new_dict))
