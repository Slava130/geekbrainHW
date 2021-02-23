dic = {}
with open('my6.txt',  encoding='utf-8') as f:
    for line in f:
        subject, hours = line.split(':')
        sum_hours = sum(map(int, ''.join([el for el in hours if el ==' ' or (el >= '0'and el <= '9')]).split()))

        dic[subject] = sum_hours
print(f'{dic}')
