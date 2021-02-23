import json


with open('my7.txt','r') as f:
        profit = {line.split()[0]:int(line.split()[2])-int(line.split()[3]) for line in f}
        total = [profit, {'average': sum([int(el) for el in profit.values() if int(el) > 0]) /
                                      len([int(el) for el in profit.values() if int(el) > 0])}]
with open('my7.json', 'w')as fj:
    json.dump(total, fj)
