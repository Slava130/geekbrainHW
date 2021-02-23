# 1 вариант
def division():
    ''' функция принимает два числа (позиционные аргументы) и выполняющую их деление '''
    a = float(input('Введите делимое:'))
    b = float(input('Введите делитель: '))
    if b != 0:
        return a / b
    else:
        print('Делить на ноль нельзя!')

print(division())



# 2 вариант

def division():
    '''  функция принимает два числа (позиционные аргументы) и выполняющую их деление '''
    try:
        a = float(input('Введите делимое:'))
        b = float(input('Введите делитель: '))
        c = a / b
    except ZeroDivisionError:
        return 'Делить на ноль нельзя!'
    return c


c = division()
print(c)
