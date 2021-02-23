from itertools import groupby

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_new_list = [el for el, _ in groupby(my_list)]  # если чесно прочел проо groupby в разных местах,но до конца не понял
print(my_new_list)
