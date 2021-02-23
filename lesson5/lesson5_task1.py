file_name = (input('Файл: ')+'.txt')
with open(file_name, 'w+') as f:
    while True:
        s = input()
        if s != '':
            f.write(s+'\n')
        else:
            break





