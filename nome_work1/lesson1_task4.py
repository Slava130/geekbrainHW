# 4-ое задание

num = int(input('Введите целое, полжительное число: '))
i = -1
while num > 0:
    d = num % 10
    num //= 10
    if d > i:
        i = d
print(i)
