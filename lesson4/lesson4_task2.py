my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result_list = [el for i, el in enumerate(my_list) if not my_list[i - 1] > my_list[i]]
print(result_list)
