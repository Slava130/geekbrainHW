class OwnError(Exception):
    def __init__(self, *args):
        self.my_list = []


    def my_input(self):
        while True:
            try:
                inp_data = input('Введите  число: ')
                if inp_data.isdigit():
                    self.my_list.append(inp_data)
                    print(f'Ваш список - {self.my_list} \n ')
                    stop = input(f'Попробовать еще раз? Y/N ')

                    if stop == 'Y' or stop == 'y':
                        continue
                    elif stop == 'N' or stop == 'n':
                        return f'Вы вышли,Ваш список- {self.my_list} '
                    break

                else:
                    raise OwnError
            except OwnError as err:
                print(f'Недопустимое значение')
                stop = input(f'Попробовать еще раз? Y/N ')

                if stop == 'Y' or stop == 'y':
                    print(self.my_input())
                elif stop == 'N' or stop == 'n':
                    return f'Вы вышли, Ваш список- {self.my_list} '
                break




a = OwnError()
a.my_input()



