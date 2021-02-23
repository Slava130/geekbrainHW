month = int(input('Введите порядковый номер месяца: '))
year = {'winter': [12, 1, 2],
        'spring': [3, 4, 5],
        'summer': [6, 7, 8],
        'autumn': [9, 10, 11],
        }

for key in year.keys():
    if month in year[key]:
        print(key)
else:
    print('Такого месяца несуществует.')
