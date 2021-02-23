worlds = input('Введите любое количество слоа через пробел: ').split()
for num, world in enumerate(worlds):
    print(num+1, world[:10])
