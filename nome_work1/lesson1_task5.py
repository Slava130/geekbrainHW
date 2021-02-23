# 5-oe задание

income = int(input('Введите сумму выручки фирмы: '))
costs = int(input('Введите сумму всех издержек фирмы: '))
profit = income - costs
if profit > 0:
    print('Фирма работает с прибылью!')
    profitability = profit / income
    print('Рентабильность фирмы : ', profitability)
    num_personal = int(input('Введите численность сотрудников фирмы: '))
    personal_profit = profit / num_personal
    print('Прибыль в расчёте на одного сотрудника составила : ', personal_profit)

elif profit == 0:
    print('Фирма работает в ноль')
else:
    print('Фирма убыточна')
