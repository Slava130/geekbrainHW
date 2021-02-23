elemen_quant = int(input(' Количество элементов списка : '))
my_list = []
count = 0
while count < elemen_quant:
    my_list.append(input('Введите элемент списка: '))
    count += 1
    print(my_list)
e = 0
for element in range(len(my_list) // 2):
    my_list[e], my_list[e + 1] = my_list[e + 1], my_list[e]
    e += 2
print(my_list)
