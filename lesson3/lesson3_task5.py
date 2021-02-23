def my_sum():
    sum1 = 0
    ex = False
    while ex == False:
        numbers = input('Введите числа через пробел или знак # чтобы завершить : ').split()

        sum2 = 0
        for number in range(len(numbers)):
            if numbers[number] == '#':
                ex = True
                break
            else:
                sum2 = sum2 + int(numbers[number])
        sum1 = sum1 + sum2
        print('Текущее значение суммы введенных чисел =', sum1)
    print('Коннечная сумма всех введённых чисел =', sum1)


my_sum()
