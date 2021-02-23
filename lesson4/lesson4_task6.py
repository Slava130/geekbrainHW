from itertools import cycle, count

iterator = (count(3))
print('Числа от 3 до 10 :', list(next(iterator) for _ in range(3, 11)))

# 2 вар
# for num in count(3):
#     if num > 10:
#         break
#     else:
#         print(num)


i = 0
for later in cycle('qwerty'):
    if i == 10:
        break
    else:
        print(later, end=' ')
    i += 1

