class Data:
    def __init__(self, dd_mm_yyyy):
        self.dd_mm_yyyy = str(dd_mm_yyyy)


    @classmethod
    def extract(cls, dd_mm_yyyy):
        my_list = []

        for i in dd_mm_yyyy.split('-'):
            my_list.append(i)

        return int(my_list[0]), int(my_list[1]), int(my_list[2])

    def __str__(self):
         return f'{Data.extract(self.dd_mm_yyyy)}'

    @staticmethod
    def valid(dd_mm_yyyy):
        my_list = []

        for i in dd_mm_yyyy.split('-'):
            my_list.append(i)

        if 1 <= int(my_list[0]) <= 31:
            if 1 <= int(my_list[1]) <= 12:
                if 2021 >= int(my_list[2]) >= 0:
                    return f'Дата верна.'
                else:
                    return f'Неверный год.'
            else:
                return f'Неверный месяц.'
        else:
            return f'Неверный день.'


data = Data('30-5-1975')
print(data)
print(data.extract('30-5-1975'))
print(data.valid('30-5-1975'))
print(data.valid('30-15-1975'))
print(Data.extract('23-3-1983'))
print(Data.valid('1-1-2023'))
