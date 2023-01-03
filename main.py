# прошлый урок
slov = {'кофе': [15.75, 7], 'мясо': [24.5, 2], 'хлеб': [2.45, 3]}
for ke, val in slov.items():
    print(f'{ke} - цена: {val[0]} - количество: {val[1]}')
while True:
    x =input("введите название продукта или 'n', если хотите завершить программу:  " )  # название или 'n'
    if x == 'n':
        break
    y = int(input('введите количество :  '))
    for ke, val in slov.items():
        if x == ke:
            z = val[0] * y
            val[1] = val[1] - y
            print('цена выбранного товара:', z)
print('остаток товара:')
for ke, val in slov.items():
    print(f'{ke} - {val[0]} - {val[1]}')