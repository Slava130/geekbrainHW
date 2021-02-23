from random import randint

with open('my5.txt', 'w+', encoding='utf-8') as f:
    #list = [str(randint(1,500)) for _ in range(1000)]
    #summ = sum(map(int(list)))
    #print(list)
    #print(summ)
    f.write(' '.join([str(randint(1, 500)) for _ in range(1000)]))
    f.seek(0)
    print(sum(map(int, f.readline().split())))


