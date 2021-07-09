containers = int(input('Кол-во контейнеров: '))
num_conteiners = []
for _ in range(containers):
    container = int(input('Введите вес контейнера: '))
    num_conteiners.append(container)
x = int(input('Введите вес нового контейнера: '))
num_conteiners = num_conteiners.append(x)
coun = 0
for num in num_conteiners:
    coun += 1
index = 0
for i in range(coun):
    if x > num_conteiners[i]:
        index = i + 1
        break
print('Номер, куда встанет новый контейнер:', index)