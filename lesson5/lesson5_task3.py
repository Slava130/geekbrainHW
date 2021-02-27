with open('my2.txt', 'r') as my_file:
    rate = []
    small = []
    my_list = my_file.read().split('\n')
    print(my_list)
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            small.append(i[0])
        rate.append(i[1])
        print(rate)
print(f'Оклад меньше 20.000 {small}, средний оклад {sum(map(int, rate)) / len(rate)}')
