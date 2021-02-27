name, price, amount, unit = None, None, None, None
my_goods, number = [], 1
while True:
    if name is None:
        name = input('Введите наименование товара:  ')
    if price is None:
        price = int(input('Введите цену товара: '))
    if amount is None:
        amount = int(input('Введите количество: '))
    if unit is None:
        unit = input('Введите ед.измерения: ')
    my_goods.append((number, {'наименование': name,
                              'цена': price,
                              'количество': amount,
                              'ед.измерения': unit}))
    name, price, amount, unit = None, None, None, None
    number += 1

    print(my_goods)

    circle = input('Формирование списка завершено? (y/n)) ')
    if circle == 'y':
        break

analitic = {'наименование': [], 'цена': [], 'количество': [], 'ед.измерения': []}
for _, item in my_goods:
    analitic['наименование'].append(item['наименование'])
    analitic['цена'].append(item['цена'])
    analitic['количество'].append(item['количество'])
    analitic['ед.измерения'].append(item['ед.измерения'])

print(analitic)
