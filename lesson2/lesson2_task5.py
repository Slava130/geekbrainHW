my_list = [13, 12, 10, 9, 7, 7, 6, 5, 3, 2, ]
number = int(input('Введите натуральное число: '))
for item in range(len(my_list)):
    if number > my_list[0]:
        my_list.insert(0, number)
    elif number < my_list[-1]:
        my_list.append(number)
    elif number == my_list[item]:
        my_list.insert(item + 1, number)
        break
    elif my_list[item] > number > my_list[item + 1]:
        my_list.insert(item + 1, number)
        break
print(my_list)
