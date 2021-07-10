containers = int(input('Кол-во контейнеров: '))
num_conteiners = []
while containers != 0:
    container = int(input('Введите вес контейнера: '))
    if container > 200:
        print('Вес контейнера не должен превышать 200кг!')
    else:
        num_conteiners.append(container)
        containers -= 1
while True:
   x = int(input('Введите вес нового контейнера: '))
   if x > 200:
       print('Вес контейнера не должен превышать 200кг!')
   else:
       break
num_conteiners.append(0)
index = 0
for i in range(len(num_conteiners)):
    if x > num_conteiners[i]:
        index = i + 1
        break

print('Номер, куда встанет новый контейнер:', index)
print('список: ', num_conteiners)