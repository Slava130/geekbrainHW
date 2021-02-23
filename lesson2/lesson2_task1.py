my_list = ['a', '2']
my_tuple = ('b', '3')
my_dict = {'city': 'Moscow', 'country': 'Russia'}
units = ['world', 234, True, 13.3, my_list, my_dict, my_tuple]
for unit in units:
    print(unit, '-', type(unit))
