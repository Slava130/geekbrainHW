with open('my.txt')as f:
    line = 0
    for i in f:
        line += 1
        space = i.count(' ')
        world = space + 1
        print(world, ' слов в ', line, 'строке')

print('В файле', line, 'строк')
